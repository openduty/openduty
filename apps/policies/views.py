from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from rest_framework import viewsets
from django.contrib.auth.models import User
from schedule.models import Calendar
from apps.policies.forms import SchedulePolicyForm
from apps.policies.serializers import SchedulePolicySerializer, SchedulePolicyRuleSerializer
from apps.policies.models import SchedulePolicy, SchedulePolicyRule


class SchedulePolicyViewSet(viewsets.ModelViewSet):
    queryset = SchedulePolicy.objects.all()
    serializer_class = SchedulePolicySerializer


class SchedulePolicyRuleViewSet(viewsets.ModelViewSet):
    queryset = SchedulePolicyRule.objects.all()
    serializer_class = SchedulePolicyRuleSerializer


class SchedulePolicyListView(LoginRequiredMixin, ListView):
    model = SchedulePolicy
    template_name = 'policies/list.html'
    context_object_name = 'policies'


class SchedulePolicyCreateOrUpdateMixin(object):

    @staticmethod
    def get_extra_context(policy):
        extra_context = {}
        if policy:
            elements = SchedulePolicyRule.objects.filter(schedule_policy=policy).order_by('position')
            calendars = Calendar.objects.all()
            groups = Group.objects.all()
            users = User.objects.all()
            extra_context = {
                'elements': elements,
                'calendars': calendars,
                'groups': groups,
                'users': users
            }
        return extra_context

    @staticmethod
    def after_form_valid(elements=[], policy=None, redirect_url='/'):
        SchedulePolicyRule.objects.filter(schedule_policy=policy).delete()
        for index, item in enumerate(elements):
            rule = SchedulePolicyRule(
                schedule_policy=policy,
                escalate_after=policy.repeat_times,
                position=index + 1,
                schedule=None,
                user_id=None,
                group_id=None
            )
            parts = item.split("|")
            if parts[0] == "user":
                rule.user_id = User.objects.get(id=parts[1])
            elif parts[0] == "calendar":
                rule.schedule = Calendar.objects.get(id=parts[1])
            elif parts[0] == "group":
                rule.group_id = Group.objects.get(id=parts[1])
            rule.save()
        return HttpResponseRedirect(redirect_url)


class SchedulePolicyCreateView(LoginRequiredMixin, CreateView, SchedulePolicyCreateOrUpdateMixin):
    model = SchedulePolicy
    form_class = SchedulePolicyForm
    template_name = 'policies/edit.html'
    success_url = '/policies/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_extra_context(self.object))
        return context

    def form_valid(self, form):
        super(SchedulePolicyCreateView, self).form_valid(form)
        return self.after_form_valid(self.request.POST.getlist('escalate_to[]'), self.object, self.get_success_url())


class SchedulePolicyUpdateView(LoginRequiredMixin, UpdateView, SchedulePolicyCreateOrUpdateMixin):
    model = SchedulePolicy
    form_class = SchedulePolicyForm
    template_name = 'policies/edit.html'
    context_object_name = 'item'
    success_url = '/policies/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_extra_context(self.get_object())
        context.update(extra_context)
        return context


class SchedulePolicyDeleteView(LoginRequiredMixin, DeleteView):
    """Delete Schedule Policy"""
    model = SchedulePolicy
    success_url = '/policies/'
