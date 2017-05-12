from openduty.auth import IsAuthenticatedOrCreateOnly

__author__ = 'deathowl'

from django.contrib.auth.models import User
from django.db import transaction
from django.utils import timezone
from notification.models import ScheduledNotification
from .escalation_helper import services_where_user_is_on_call
from .models import (Incident, Service, ServiceTokens, Token, EventLog,
                     IncidentSilenced, ServiceSilenced)
from rest_framework import viewsets
from .serializers import IncidentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.core.exceptions import ValidationError
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from notification.helper import NotificationHelper
from openduty.tasks import unsilence_incident
import uuid
import base64
from .tables import IncidentTable

from django_tables2_simplefilter import FilteredSingleTableView

class IncidentViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows incidents to be viewed or edited.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = (IsAuthenticatedOrCreateOnly,)

    def is_relevant(self, incident, new_event_type):
        """
        Check incident conditions
        :param incident: Actual incident
        :param new_event_type: Reported event_type
        :return: True if relevant else False
        """
        # There is already an incident
        if incident.event_type:
            # True if not acknowleged or type is resolve
            return (incident.event_type != Incident.ACKNOWLEDGE or
                    (incident.event_type == Incident.ACKNOWLEDGE and
                     new_event_type == Incident.RESOLVE) or (incident.event_type == Incident.ACKNOWLEDGE and new_event_type == Incident.UNACKNOWLEDGE))
        # New incident
        else:
            # True if this is a trigger action
            return new_event_type == Incident.TRIGGER

    def create(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(key=request.DATA["service_key"])
            serviceToken = ServiceTokens.objects.get(token_id=token)
            service = serviceToken.service_id
        except ServiceTokens.DoesNotExist:
            return Response({"Service key does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Token.DoesNotExist:
            return Response({"No service key"}, status=status.HTTP_403_FORBIDDEN)

        with transaction.atomic():
            try:
                esc = False
                incident = Incident.objects.get(incident_key=request.DATA["incident_key"],service_key=service)
                print "Received %s for %s on service %s" % (request.DATA['event_type'],request.DATA['incident_key'],serviceToken.name)
                #check if type is ACK or resolve and if there's an escalation to a different escalation policy, remove it
                if request.DATA['event_type'] == Incident.ACKNOWLEDGE or request.DATA['event_type'] == Incident.RESOLVE:
                    print "ACK or Resolve, removing specific escalation"
                    esc = True
                    incident.service_to_escalate_to = None
                    incident.save()
                # check if incident is resolved and refuse to ACK
                if not (incident.event_type == Incident.RESOLVE and request.DATA['event_type'] == Incident.ACKNOWLEDGE):
                    event_log_message = "%s api key changed %s from %s to %s" % (
                        serviceToken.name, incident.incident_key,
                        incident.event_type, request.DATA['event_type'])
                    if esc:
                        event_log_message += ", unescalated"
                else:
                    response = {}
                    response["status"] = "failure"
                    response["message"] = "Can\'t ACK a resolved incident!"
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
            except (Incident.DoesNotExist, KeyError):
                incident = Incident()
                try:
                    incident.incident_key = request.DATA["incident_key"]
                except KeyError:
                    if request.DATA["event_type"] == Incident.TRIGGER:
                        incident.incident_key = base64.urlsafe_b64encode(
                            uuid.uuid1().bytes).replace(
                            '=',
                            '')
                    else:
                        response = {}
                        response["status"] = "failure"
                        response["message"] = "Mandatory parameter missing"
                        return Response(
                            response,
                            status=status.HTTP_400_BAD_REQUEST)
                incident.service_key = service

                event_log_message = "%s api key created %s with status %s" % (
                    serviceToken.name, incident.incident_key, request.DATA['event_type'])

            if self.is_relevant(incident, request.DATA['event_type']):
                event_log = EventLog()
                # Anonymous user for testing
                if request.user.is_anonymous():
                    user = None
                else:
                    user = request.user
                event_log.user = user
                event_log.service_key = incident.service_key
                event_log.data = event_log_message
                event_log.occurred_at = timezone.now()

                incident.event_type = request.DATA["event_type"]
                incident.description = request.DATA["description"][:100]
                incident.details = request.DATA.get("details", "")
                incident.occurred_at = timezone.now()
                try:
                    incident.full_clean()
                except ValidationError as e:
                    return Response(
                        {'errors': e.messages},
                        status=status.HTTP_400_BAD_REQUEST)
                incident.save()
                event_log.incident_key = incident
                event_log.action = incident.event_type
                event_log.save()
                servicesilenced = ServiceSilenced.objects.filter(
                    service=service).count() > 0
                if incident.event_type == Incident.TRIGGER and not servicesilenced:
                    NotificationHelper.notify_incident(incident)
                if incident.event_type == Incident.RESOLVE or incident.event_type == Incident.ACKNOWLEDGE:
                    ScheduledNotification.remove_all_for_incident(incident)
                    if incident.event_type == Incident.RESOLVE and service.send_resolve_enabled:
                        NotificationHelper.notify_incident(incident)

            headers = self.get_success_headers(request.POST)

            response = {}
            response["status"] = "success"
            response["message"] = "Event processed"
            response["incident_key"] = incident.incident_key
            return Response(response,status=status.HTTP_201_CREATED,headers=headers)


    #escalate an incident to another service's escalation rule; persists until ACK
    @detail_route(methods=['put'])
    def escalate(self, request, *args, **kwargs):
        #get arguments
        try:
            token = Token.objects.get(key=request.DATA["service_key"])
            serviceToken = ServiceTokens.objects.get(token_id=token)
            service = serviceToken.service_id
        except ServiceTokens.DoesNotExist:
            return Response({"Service key does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Token.DoesNotExist:
            return Response({"No service key"}, status=status.HTTP_403_FORBIDDEN)

        try:
            token2 = Token.objects.get(key=request.DATA["service_key_to_escalate_to"])
            serviceToken2 = ServiceTokens.objects.get(token_id=token2)
            service2 = serviceToken2.service_id
        except ServiceTokens.DoesNotExist:
            return Response({"Service to escalate to key does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Token.DoesNotExist:
            return Response({"No service to escalate to key"}, status=status.HTTP_403_FORBIDDEN)

        #modify incident
        with transaction.atomic():
            try:
                # get service_to_escalate to and modify incident object
                incident = Incident.objects.get(incident_key=request.DATA["incident_key"],service_key=service)
                incident.service_to_escalate_to = service2
                incident.event_type = "escalated"
                if request.DATA["incident_details"]:
                    incident.details = request.DATA["incident_details"]
#                incident.description = "[escalated] " + incident.description
                incident.save()

                event_log_message = "%s escalated to service escalation policy :  %s  to %s" % (request.user.username, incident.incident_key, service2.name)
                event_log = EventLog()
                event_log.user = request.user
                event_log.action = "escalate"
                event_log.incident_key = incident
                event_log.service_key = incident.service_key
                event_log.data = event_log_message
                event_log.occurred_at = timezone.now()
                event_log.save()

            except (Incident.DoesNotExist, KeyError):
                return Response({"Incident does not exist"}, status=status.HTTP_404_NOT_FOUND)
            except (Service.DoesNotExist, KeyError):
                return Response({"Service does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        # remove all planned notifs
        ScheduledNotification.remove_all_for_incident(incident)
        # notify anew, this time notify_incident will detect the service_to_escalate to and notify its escalation rule
        NotificationHelper.notify_incident(incident)

        headers = self.get_success_headers(request.POST)

        return Response({"Incident successfully escalated to service " + service2.name + " escalation policy"},status=status.HTTP_200_OK,headers=headers)


class ServicesByMe(FilteredSingleTableView):
    model = Incident
    table_class = IncidentTable
    template_name='incidents/list2.html'
    table_pagination={"per_page": 10}

    def get_queryset(self):
        user = self.request.user
        q = super(ServicesByMe, self).get_queryset()
        services = services_where_user_is_on_call(user)
        incidents = q.filter(service_key__in=services)
        incidents = incidents.order_by("-occurred_at")
        return incidents


@login_required()
def details(request, id):
    try:
        incident = Incident.objects.get(id=id)
        try:
            service_silenced = ServiceSilenced.objects.get(service=incident.service_key).silenced
        except ServiceSilenced.DoesNotExist:
            service_silenced = False
        try:
            is_obj = IncidentSilenced.objects.get(incident=incident)
            incident_silenced = str(is_obj.silenced_until - timezone.now()).split(".")[0]
        except IncidentSilenced.DoesNotExist:
            incident_silenced = False
        users = User.objects.all()
        history = EventLog.objects.filter(
            incident_key=incident).order_by('-occurred_at')
        return TemplateResponse(request, 'incidents/details.html', {
            'item': incident, 'users': users, 'url': request.get_full_path(),
            'history_list': history, 'service_silenced': service_silenced,
            'incident_silenced': incident_silenced
        })
    except Service.DoesNotExist:
        raise Http404


def _update_type(user, ids, event_type):
    for incident_id in ids:
        with transaction.atomic():
            incident = Incident.objects.get(id=int(incident_id))
            unesc = False
            if incident.service_to_escalate_to is not None:
                incident.service_to_escalate_to = None
                unesc = True
            logmessage = EventLog()
            logmessage.service_key = incident.service_key
            logmessage.user = user
            logmessage.action = event_type
            logmessage.data = "%s changed %s from %s to %s" % (
                user.username,
                incident.incident_key,
                incident.event_type,
                event_type)
            if unesc:
                logmessage.data += ", unescalated"
            logmessage.occurred_at = timezone.now()

            incident.event_type = event_type
            incident.occurred_at = timezone.now()
            incident.save()

            logmessage.incident_key = incident
            logmessage.save()
            if incident.event_type == Incident.RESOLVE or incident.event_type == Incident.ACKNOWLEDGE:
                ScheduledNotification.remove_all_for_incident(incident)


@login_required()
@require_http_methods(["POST"])
def update_type(request):
    event_type = request.POST['event_type']
    event_types = ('acknowledge', 'resolve')
    incident_ids = request.POST.getlist('selection', None)
    if not event_type:
        messages.error(request, 'Invalid event modification!')
        return HttpResponseRedirect(request.POST['url'])
    try:
        if incident_ids:
            for id in incident_ids:
                with transaction.atomic():
                    incident = Incident.objects.get(id=id)
                    if incident.event_type == 'resolve' and event_type == 'acknowledge':
                        messages.error(request, 'Can\' ACK a resolved incident!')
                        return HttpResponseRedirect(request.POST['url'])
                    else:
                        _update_type(request.user, incident_ids, event_type)
        else:
            id = request.POST.get('id')
            incident = Incident.objects.get(id=id)
            if incident.event_type == 'resolve' and event_type == 'acknowledge':
                messages.error(request, 'Can\' ACK a resolved incident!')
                return HttpResponseRedirect(request.POST['url'])
            else:
                _update_type(request.user, [id], event_type)
    except Incident.DoesNotExist:
        messages.error(request, 'Incident not found')
        return HttpResponseRedirect(request.POST['url'])
    except ValidationError as e:
        messages.error(request, e.messages)
    return HttpResponseRedirect(request.POST['url'])


@login_required()
@require_http_methods(["POST"])
def forward_incident(request):
    try:
        with transaction.atomic():
            incident = Incident.objects.get(id=request.POST['id'])
            user = User.objects.get(id=request.POST['user_id'])
            ScheduledNotification.remove_all_for_incident(incident)
            NotificationHelper.notify_user_about_incident(incident, user)
            event_log_message = "%s  changed assignee of incident :  %s  to %s" % (
                request.user.username, incident.incident_key, user.username)
            event_log = EventLog()
            event_log.user = request.user
            event_log.action = "forward"
            event_log.incident_key = incident
            event_log.service_key = incident.service_key
            event_log.data = event_log_message
            event_log.occurred_at = timezone.now()
            event_log.save()

    except Incident.DoesNotExist:
        messages.error(request, 'Incident not found')
        return HttpResponseRedirect(request.POST['url'])
    except User.DoesNotExist:
        messages.error(request, 'Incident not found')
        return HttpResponseRedirect(request.POST['url'])
    except ValidationError as e:
        messages.error(request, e.messages)
    return HttpResponseRedirect(request.POST['url'])


@login_required()
@require_http_methods(["POST"])
def silence(request, incident_id):
    try:
        incident = Incident.objects.get(id=incident_id)
        silence_for = request.POST.get('silence_for')
        url = request.POST.get("url")
        if IncidentSilenced.objects.filter(incident=incident).count() < 1:
            silenced_incident = IncidentSilenced()
            silenced_incident.incident = incident
            silenced_incident.silenced_until = timezone.now(
                ) + timezone.timedelta(hours=int(silence_for))
            silenced_incident.silenced = True
            silenced_incident.save()
            event_log_message = "%s silenced incident %s for %s hours" % (
                request.user.username, incident.incident_key, silence_for)
            event_log = EventLog()
            event_log.incident_key = incident
            event_log.action = 'silence_incident'
            event_log.user = request.user
            event_log.service_key = incident.service_key
            event_log.data = event_log_message
            event_log.occurred_at = timezone.now()
            event_log.save()
            ScheduledNotification.remove_all_for_incident(incident)
            incident.event_type = Incident.ACKNOWLEDGE
            incident.save()
            unsilence_incident.apply_async(
                (incident_id,), eta=silenced_incident.silenced_until)
        return HttpResponseRedirect(url)
    except Service.DoesNotExist:
        raise Http404

@login_required()
@require_http_methods(["POST"])
def unsilence(request, incident_id):
    try:
        incident = Incident.objects.get(id = incident_id)
        url = request.POST.get("url")
        try:
            IncidentSilenced.objects.filter(incident=incident).delete()
            event_log_message = "%s removed silence from incident %s" % (request.user.username, incident.incident_key)
            event_log = EventLog()
            event_log.action = 'unsilence_incident'
            event_log.user = request.user
            event_log.incident_key = incident
            event_log.service_key = incident.service_key
            event_log.data = event_log_message
            event_log.occurred_at = timezone.now()
            event_log.save()
        except IncidentSilenced.DoesNotExist:
            # No need to delete
            pass
        return HttpResponseRedirect(url)
    except Service.DoesNotExist:
        raise Http404
