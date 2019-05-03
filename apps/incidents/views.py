import uuid
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from apps.notification.models import ScheduledNotification
from apps.notification.helper import NotificationHelper
from apps.services.models import ServiceSilenced, ServiceTokens
from apps.events.models import EventLog
from apps.services.models import Token
from apps.openduty.tasks import unsilence_incident
from apps.incidents.serializers import IncidentSerializer
from apps.incidents.escalation_helper import services_where_user_is_on_call
from apps.incidents.models import Incident, IncidentSilenced


class IncidentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows incidents to be viewed or edited.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def is_relevant(self, incident, new_event_type):
        """
        Check incident conditions
        :param incident: Actual incident
        :param new_event_type: Reported event_type
        :return: True if relevant else False
        """
        valid_list = [Incident.ACKNOWLEDGE, Incident.RESOLVE, Incident.TRIGGER, Incident.UNACKNOWLEDGE, Incident.ESCALATE]
        # There is already an incident
        if incident.event_type and incident.event_type in valid_list:
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
            assert request.data.get("event_type")
            assert request.data.get("incident_key")
            assert request.data.get("service_key")
        except AssertionError:
            response = {"status": "failure", "message": "Mandatory parameter missing"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = Token.objects.get(key=request.data.get("service_key"))
            service_token = ServiceTokens.objects.get(token_id=token)
            service = service_token.service_id
        except Token.DoesNotExist:
            return Response({"No service key"}, status=status.HTTP_403_FORBIDDEN)
        except ServiceTokens.DoesNotExist:
            return Response({"Service key does not exist"}, status=status.HTTP_404_NOT_FOUND)

        esc = False
        incidents = Incident.objects.filter(
            incident_key=request.data.get("incident_key"), service_key=service
        )
        if incidents:
            incident = incidents[0]
            print(f"Received {request.data.get('event_type')} for"
                  f" {request.data.get('incident_key')} on service {service_token.name}")
            # check if type is ACK or resolve and if there's an
            # escalation to a different escalation policy, remove it
            if request.data.get('event_type') in [Incident.ACKNOWLEDGE, Incident.RESOLVE]:
                print("ACK or Resolve, removing specific escalation")
                esc = True
                incident.service_to_escalate_to = None
                incident.save()
            # check if incident is resolved and refuse to ACK
            event_log_message = f"{service_token.name} api key changed {incident.incident_key} " \
                f"from {incident.event_type} to {request.data.get('event_type')}"
            if incident.event_type not in [Incident.RESOLVE, Incident.ACKNOWLEDGE] and esc:
                event_log_message += ", unescalated"
        else:
            event_type = request.data.get("event_type")
            incident_key = str(uuid.uuid1()) if (event_type == Incident.TRIGGER) else request.data.get("incident_key")
            incident_service_key = service
            incident = Incident.objects.create(
                event_type=event_type,
                incident_key=incident_key,
                service_key=incident_service_key,
                description=request.data.get("description", " "),
                details=request.data.get("details", " "),
                occurred_at=timezone.now()
            )
            event_log_message = f"{service_token.name} api key created " \
                f"{incident.incident_key} with status {request.data.get('event_type')}"

        if self.is_relevant(incident, request.data.get('event_type')):
            user = None if request.user.is_anonymous else request.user
            event_log = EventLog(
                user=user,
                service_key=incident.service_key,
                data=event_log_message,
                occurred_at=timezone.now()
            )
            event_log.incident_key = incident
            event_log.action = incident.event_type
            event_log.save()
            service_silenced = ServiceSilenced.objects.filter(service=service).count() > 0
            if incident.event_type == Incident.TRIGGER and not service_silenced:
                NotificationHelper.notify_incident(incident)
            if incident.event_type == Incident.RESOLVE or incident.event_type == Incident.ACKNOWLEDGE:
                ScheduledNotification.remove_all_for_incident(incident)
                if incident.event_type == Incident.RESOLVE and service.send_resolve_enabled:
                    NotificationHelper.notify_incident(incident)

        response = {"status": "success", "message": "Event processed", "incident_key": incident.incident_key}
        return Response(response, status=status.HTTP_201_CREATED)

    @detail_route(methods=['put'])
    def escalate(self, request, *args, **kwargs):
        """
        escalate an incident to another service's escalation rule; persists until ACK
        """
        try:
            token = Token.objects.get(key=request.data.get("service_key"))
            service_token = ServiceTokens.objects.get(token_id=token)
            service = service_token.service_id
        except ServiceTokens.DoesNotExist:
            return Response({"Service key does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Token.DoesNotExist:
            return Response({"No service key"}, status=status.HTTP_403_FORBIDDEN)

        try:
            token2 = Token.objects.get(key=request.data.get("service_key_to_escalate_to"))
            service_token2 = ServiceTokens.objects.get(token_id=token2)
            service2 = service_token2.service_id
        except ServiceTokens.DoesNotExist:
            return Response({"Service to escalate to key does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Token.DoesNotExist:
            return Response({"No service to escalate to key"}, status=status.HTTP_403_FORBIDDEN)
        try:
            # get service_to_escalate to and modify incident object
            incident = Incident.objects.get(incident_key=request.data.get("incident_key"), service_key=service)
        except (Incident.DoesNotExist, KeyError):
            return Response({"Incident does not exist"}, status=status.HTTP_404_NOT_FOUND)
        incident.service_to_escalate_to = service2
        incident.event_type = "escalated"
        if request.data.get("IncidentDetailView"):
            incident.details = request.data.get("IncidentDetailView")
        incident.save()
        username = 'no user' if request.user.is_anonymous else request.user.username
        event_log_message = f"{username} escalated to " \
            f"service escalation policy :  {incident.incident_key}  to {service2.name}"
        EventLog.objects.create(
            user=request.user,
            action="escalate",
            incident_key=incident,
            service_key=incident.service_key,
            data=event_log_message,
            occurred_at=timezone.now()
        )
        # remove all planned notifs
        ScheduledNotification.remove_all_for_incident(incident)
        # notify anew, this time notify_incident will detect the service_to_escalate to and notify its escalation rule
        NotificationHelper.notify_incident(incident)

        headers = self.get_success_headers(request.POST)

        return Response(
            {f"Incident successfully escalated to service {service2.name} escalation policy"},
            status=status.HTTP_200_OK,
            headers=headers
        )


class OnCallIncidentsListView(LoginRequiredMixin, ListView):
    model = Incident
    context_object_name = 'all_incidents'
    template_name = 'incidents/list.html'

    def get_queryset(self, *args, **kwargs):
        services = services_where_user_is_on_call(self.request.user)
        queryset = Incident.objects.filter(service_key__in=services).order_by("-occurred_at")
        return queryset


class IncidentsListView(LoginRequiredMixin, ListView):
    model = Incident
    queryset = Incident.objects.all().order_by('id')
    template_name = 'incidents/list.html'
    context_object_name = 'all_incidents'


class IncidentDetailView(LoginRequiredMixin, DetailView):
    model = Incident
    template_name = 'incidents/details.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(IncidentDetailView, self).get_context_data(**kwargs)
        incident = self.object
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
        extra_context = {
            'item': incident,
            'users': users,
            'url': self.request.get_full_path(),
            'history_list': history,
            'service_silenced': service_silenced,
            'incident_silenced': incident_silenced
        }
        context.update(extra_context)
        return context


def _update_type(user, ids, event_type):
    for incident_id in ids:
        incident = Incident.objects.get(id=int(incident_id))
        log_message_data = f"{user.username} changed {incident.incident_key} from {incident.event_type} to {event_type}"
        if incident.service_to_escalate_to is not None:
            incident.service_to_escalate_to = None
            log_message_data += ", unescalated"
        EventLog.objects.create(
            service_key=incident.service_key,
            user=user,
            action=event_type,
            data=log_message_data,
            occurred_at=timezone.now(),
            incident_key=incident
        )
        incident.event_type = event_type
        incident.occurred_at = timezone.now()
        incident.save()
        if incident.event_type == Incident.RESOLVE or incident.event_type == Incident.ACKNOWLEDGE:
            ScheduledNotification.remove_all_for_incident(incident)


# TODO: Needs Refactoring work + changed update_type url
@login_required()
@require_http_methods(["POST"])
def update_type(request):
    event_type = request.POST.get('event_type')
    incident_ids = request.POST.getlist('selection', [])
    incident_ids.append(request.POST.get('id'))
    url = reverse('IncidentsListView')
    request_url = request.POST.get('url', url)
    if event_type is None:
        messages.error(request, 'Invalid event modification!')
        return HttpResponseRedirect(request_url)
    try:
        for pk in incident_ids:
            incident = Incident.objects.get(id=pk)
            if incident.event_type == 'resolve' and event_type == 'acknowledge':
                messages.error(request, 'Can\' ACK a resolved incident!')
                return HttpResponseRedirect(request_url)
            else:
                _update_type(request.user, incident_ids, event_type)
    except Incident.DoesNotExist:
        messages.error(request, 'Incident not found')
    return HttpResponseRedirect(request_url)


# TODO: Needs Refactoring work + changed forward_incident url
@login_required()
@require_http_methods(["POST"])
def forward_incident(request):
    url = reverse('IncidentsListView')
    request_url = request.POST.get('url', url)
    try:
        incident = Incident.objects.get(id=request.POST.get('id'))
        user = User.objects.get(id=request.POST.get('user_id'))
        ScheduledNotification.remove_all_for_incident(incident)
        NotificationHelper.notify_user_about_incident(incident, user)
        event_log_message = f"{request.user.username} changed assignee of " \
            f"incident : {incident.incident_key} to {user.username}"
        EventLog.objects.create(
            user=request.user,
            action="forward",
            incident_key=incident,
            service_key=incident.service_key,
            data=event_log_message,
            occurred_at=timezone.now()
        )
    except Incident.DoesNotExist:
        messages.error(request, 'Incident not found')
        return HttpResponseRedirect(request_url)
    except User.DoesNotExist:
        messages.error(request, 'Incident not found')
        return HttpResponseRedirect(request_url)
    return HttpResponseRedirect(request_url)


# TODO: Needs Refactoring work + changed silence url
@login_required()
@require_http_methods(["POST"])
def silence(request, incident_id):
    silence_for = request.POST.get('silence_for', 0)
    url = reverse('IncidentsListView')
    request_url = request.POST.get('url', url)
    try:
        incident = Incident.objects.get(id=int(incident_id))
    except Incident.DoesNotExist:
        messages.error(request, 'Incident not found')
        return HttpResponseRedirect(request_url)
    if IncidentSilenced.objects.filter(incident=incident).count() < 1:
        silenced_incident = IncidentSilenced.objects.create(
            incident=incident,
            silenced_until=timezone.now() + timezone.timedelta(hours=int(silence_for)),
            silenced=True
        )
        event_log_message = f"{request.user.username} silenced " \
            f"incident {incident.incident_key} for {silence_for} hours"
        EventLog.objects.create(
            incident_key=incident,
            action='silence_incident',
            user=request.user,
            service_key=incident.service_key,
            data=event_log_message,
            occurred_at=timezone.now()
        )
        ScheduledNotification.remove_all_for_incident(incident)
        incident.event_type = Incident.ACKNOWLEDGE
        incident.save()
        unsilence_incident.apply_async((incident_id,), eta=silenced_incident.silenced_until)
        messages.success(request, event_log_message)
    return HttpResponseRedirect(request_url)


# TODO: Needs Refactoring work + changed unsilence url
@login_required()
@require_http_methods(["POST"])
def unsilence(request, incident_id):
    url = reverse('IncidentsListView')
    request_url = request.POST.get('url', url)
    try:
        incident = Incident.objects.get(id=incident_id)
    except Incident.DoesNotExist:
        messages.error(request, 'Incident not found')
        return HttpResponseRedirect(request_url)
    IncidentSilenced.objects.filter(incident=incident).delete()
    event_log_message = f"{request.user.username} removed silence from incident {incident.incident_key}"
    EventLog.objects.create(
        action='unsilence_incident',
        user=request.user,
        incident_key=incident,
        service_key=incident.service_key,
        data=event_log_message,
        occurred_at=timezone.now()
    )
    messages.success(request, event_log_message)
    return HttpResponseRedirect(request_url)
