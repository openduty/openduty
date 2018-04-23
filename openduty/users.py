from notification.helper import NotificationHelper

__author__ = "dzsubek"

from notification.models import UserNotificationMethod
from notification.notifier.hipchat import HipchatNotifier
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from .models import User, UserProfile
from django.contrib.auth.models import Group
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
import itertools


@login_required()
def list(request):
    users = User.objects.all();
    return TemplateResponse(request, 'users/list.html', {'users': users})

@login_required()
@staff_member_required
def delete(request, id):
    try:
        user = User.objects.get(id = id)
        user.delete()
        return HttpResponseRedirect('/users/');
    except User.DoesNotExist:
        raise Http404

@login_required()
def edit(request, id):
    if not request.user.is_staff and int(request.user.id) != int(id):
        raise PermissionDenied("User " + str(request.user.id) + " isn't staff")
    try:
        user = User.objects.get(id = id)
        user_methods = UserNotificationMethod.objects.filter(user = user).order_by('position')
        all_groups = Group.objects.all()
        user_groups = [str(x.name) for x in User.objects.get(id=id).groups.all()]
        return TemplateResponse(
            request, 'users/edit.html',
            {'item': user, 'all_groups': all_groups, 'user_groups': user_groups, 'methods': UserNotificationMethod.methods, 'user_methods': user_methods, 'empty_user_method': UserNotificationMethod(), 'hipchat_rooms': HipchatNotifier(settings.HIPCHAT_SETTINGS).get_all_rooms()}
        )
    except User.DoesNotExist:
        raise Http404

@login_required()
@staff_member_required
def new(request):
    return TemplateResponse(request, 'users/edit.html', {'methods': UserNotificationMethod.methods, 'empty_user_method': UserNotificationMethod(), 'hipchat_rooms': HipchatNotifier (settings.HIPCHAT_SETTINGS).get_all_rooms()})

@login_required()
@require_http_methods(["POST"])
def save(request):
    if not request.user.is_staff and int(request.user.id) != int(request.POST['id']):
        raise PermissionDenied("User " + str(request.user.id) + " isn't staff")
    try:
        user = User.objects.get(id = request.POST['id'])
    except User.DoesNotExist:
        user = User()
        user.is_active = True

    user.username = request.POST['username']
    user.email = request.POST['email']
    if request.POST['password']:
        user.set_password(request.POST['password'])

    try:
        user.save()
        all_groups = []
        for group in Group.objects.all():
            all_groups.append(int(group.id))
        post_groups = request.POST.getlist('groups[]')
        for idx, group in enumerate(post_groups):
            group = int(group)
            if group in all_groups:
                all_groups.remove(group)
            if group not in [x.id for x in User.objects.get(id=request.POST['id']).groups.all()]:  #Groups.objects.filter(id__in=user.groups.all().values_list('id', flat=True))]:
                try:
                    user.groups.add(group)
                except e:
                    messages.error(request, str(e))

        if len(all_groups) > 0:
            for group in all_groups:
                user.groups.remove(group)

        user.save()
        try:
            UserNotificationMethod.objects.filter(user=user).delete()
        except UserNotificationMethod.DoesNotExist:
            pass #Nothing to clear
        methods = request.POST.getlist('methods[]')
        for idx, item in enumerate(methods):
            method = UserNotificationMethod()
            method.method = item
            method.user = user
            method.position = idx +1
            method.save()

        if user.profile is None:
            profile = UserProfile()
            profile.user = user
        else:
            profile = user.profile

        profile.phone_number = request.POST['phone_number']
        profile.pushover_user_key = request.POST['pushover_user_key']
        profile.pushover_app_key = request.POST['pushover_app_key']
        profile.slack_room_name = request.POST['slack_room_name']
        profile.prowl_api_key = request.POST['prowl_api_key']
        profile.prowl_application = request.POST['prowl_application']
        profile.prowl_url = request.POST['prowl_url']
        profile.rocket_webhook_url = request.POST['rocket_webhook_url']
        profile.hipchat_room_name = request.POST['hipchat_room_name']
        profile.hipchat_room_url = request.POST['hipchat_room_url']
        profile.send_resolve_enabled = request.POST.get("send_resolve_notification", "off") == "on"
        profile.save()

        return HttpResponseRedirect(reverse('openduty.users.list'))
    except IntegrityError:
        messages.error(request, 'Username already exists.')
        if int(request.POST['id']) > 0:
            return HttpResponseRedirect(reverse('openduty.users.edit', None, [str(request.POST['id'])]))
        else:
            return HttpResponseRedirect(reverse('openduty.users.new'))

@login_required()
@require_http_methods(["POST"])
def testnotification(request):
    if not request.user.is_staff and int(request.user.id) != int(request.POST['id']):
        raise PermissionDenied("User " + str(request.user.id) + " isn't staff")
    user = User.objects.get(id=request.POST['id'])
    NotificationHelper.notify_user_about_incident(None, user, 1, "This is a notification test message, just ignore it")
    return HttpResponseRedirect(reverse('openduty.users.list'))
