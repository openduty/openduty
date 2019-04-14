from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from braces.views import StaffuserRequiredMixin
from apps.accounts.serializers import UserSerializer, GroupSerializer
from apps.accounts.models import Profile
from apps.notification.helper import NotificationHelper
from apps.notification.models import UserNotificationMethod
from apps.notification.notifier.hipchat import HipchatNotifier
from apps.accounts.forms import CustomAuthenticationForm, UserProfileMultiForm


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


class UserDeleteView(StaffuserRequiredMixin, DeleteView):
    """Delete User"""
    model = User
    template_name = 'users/delete.html'
    success_url = '/users/'


class UserEditView(StaffuserRequiredMixin, UpdateView):
    model = User
    template_name = 'users/edit.html'
    context_object_name = 'item'
    form_class = UserProfileMultiForm
    success_url = reverse_lazy('UserListView')

    def form_valid(self, form):
        # Save the user first, because the profile needs a user before it
        # can be saved.
        user = form['user'].save()
        if form['user'].cleaned_data.get('password'):
            user.set_password(form['user'].cleaned_data.get('password'))
            user.save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()
        all_groups = []
        for group in Group.objects.all():
            all_groups.append(int(group.id))
        post_groups = self.request.POST.getlist('groups[]')
        for idx, group in enumerate(post_groups):
            group = int(group)
            if group in all_groups:
                all_groups.remove(group)
            if group not in [x.id for x in User.objects.get(id=self.object.id).groups.all()]:
                try:
                    user.groups.add(group)
                except Exception as e:  # pragma: no cover
                    messages.error(self.request, str(e))
        if len(all_groups) > 0:
            for group in all_groups:
                user.groups.remove(group)
        user.save()
        try:
            UserNotificationMethod.objects.filter(user=user).delete()
        except UserNotificationMethod.DoesNotExist:  # pragma: no cover
            pass  # Nothing to clear
        methods = self.request.POST.getlist('methods[]')
        for idx, item in enumerate(methods):
            method = UserNotificationMethod()
            method.method = item
            method.user = user
            method.position = idx + 1
            method.save()
        return redirect(self.success_url)

    def get_form_kwargs(self):
        kwargs = super(UserEditView, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object,
            'profile': self.object.profile,
        })
        return kwargs

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


class UserCreateView(StaffuserRequiredMixin, CreateView):
    template_name = 'users/edit.html'
    context_object_name = 'item'
    form_class = UserProfileMultiForm
    success_url = reverse_lazy('UserListView')

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        custom_context = {
            'methods': UserNotificationMethod.methods,
            'empty_user_method': UserNotificationMethod(),
            'hipchat_rooms': HipchatNotifier(settings.HIPCHAT_SETTINGS).get_all_rooms()
        }
        context.update(custom_context)

    def form_valid(self, form):
        user = form['user'].save()
        if form['user'].cleaned_data.get('password'):
            user.set_password(form['user'].cleaned_data.get('password'))
            user.save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()
        return redirect(self.success_url)


@login_required()
@require_http_methods(["POST"])
def testnotification(request):  # pragma: no cover
    if not request.user.is_staff and int(request.user.id) != int(request.POST['id']):
        raise PermissionDenied("User " + str(request.user.id) + " isn't staff")
    user = User.objects.get(id=request.POST['id'])
    NotificationHelper.notify_user_about_incident(None, user, 1, "This is a notification test message, just ignore it")
    return HttpResponseRedirect(reverse('UserListView'))


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = CustomAuthenticationForm


def logout(request):  # pragma: no cover
    auth_logout(request)
    return HttpResponseRedirect('/login/')
