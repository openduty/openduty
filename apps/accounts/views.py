from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, Group
from apps.accounts.serializers import UserSerializer, GroupSerializer
from apps.accounts.models import UserProfile
from apps.notification.helper import NotificationHelper
from apps.notification.models import UserNotificationMethod
from apps.notification.notifier.hipchat import HipchatNotifier
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import LoginView
from apps.accounts.forms import CustomAuthenticationForm


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserListView(LoginRequiredMixin, ListView):
    """Users List"""
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'


class UserIsAdminMixin(AccessMixin):  # pragma: no cover
    """Verify that the current user is authenticated and Admin."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(UserIsAdminMixin, DeleteView):
    """Delete User"""
    model = User
    template_name = 'users/delete.html'
    success_url = '/users/'


class UserEditView(UserIsAdminMixin, UpdateView):
    model = User
    template_name = 'users/edit.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(UserEditView, self).get_context_data(**kwargs)
        user_methods = UserNotificationMethod.objects.filter(user=self.object).order_by('position')
        all_groups = Group.objects.all()
        user_groups = [str(x.name) for x in self.object.groups.all()]
        custom_context = {
            'all_groups': all_groups,
            'user_groups': user_groups,
            'methods': UserNotificationMethod.methods,
            'user_methods': user_methods,
            'empty_user_method': UserNotificationMethod(),
            'hipchat_rooms': HipchatNotifier(settings.HIPCHAT_SETTINGS).get_all_rooms()
        }
        context.update(custom_context)
        return context


class UserCreateView(UserIsAdminMixin, CreateView):
    model = User
    template_name = 'users/edit.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        custom_context = {
            'methods': UserNotificationMethod.methods,
            'empty_user_method': UserNotificationMethod(),
            'hipchat_rooms': HipchatNotifier(settings.HIPCHAT_SETTINGS).get_all_rooms()
        }
        context.update(custom_context)


@login_required()
@require_http_methods(["POST"])
def save(request):
    if not request.user.is_staff and int(request.user.id) != int(request.POST['id']):
        raise PermissionDenied("User " + str(request.user.id) + " isn't staff")
    try:
        user = User.objects.get(id=int(request.POST['id']))
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
                except Exception as e:
                    messages.error(request, str(e))

        if len(all_groups) > 0:
            for group in all_groups:
                user.groups.remove(group)

        user.save()
        try:
            UserNotificationMethod.objects.filter(user=user).delete()
        except UserNotificationMethod.DoesNotExist:  # pragma: no cover
            pass  # Nothing to clear
        methods = request.POST.getlist('methods[]')
        for idx, item in enumerate(methods):
            method = UserNotificationMethod()
            method.method = item
            method.user = user
            method.position = idx +1
            method.save()

        try:
            profile = user.profile
        except ObjectDoesNotExist:
            profile = UserProfile()
            profile.user = user
            profile.save()

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

        return HttpResponseRedirect(reverse('UserListView'))
    except IntegrityError:
        messages.error(request, 'Username already exists.')
        if int(request.POST['id']) > 0:
            return HttpResponseRedirect(reverse('UserEditView', None, [str(request.POST['id'])]))
        else:
            return HttpResponseRedirect(reverse('UserCreateView'))


@login_required()
@require_http_methods(["POST"])
def testnotification(request):
    if not request.user.is_staff and int(request.user.id) != int(request.POST['id']):
        raise PermissionDenied("User " + str(request.user.id) + " isn't staff")
    user = User.objects.get(id=request.POST['id'])
    NotificationHelper.notify_user_about_incident(None, user, 1, "This is a notification test message, just ignore it")
    return HttpResponseRedirect(reverse('UserListView'))


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = CustomAuthenticationForm


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')
