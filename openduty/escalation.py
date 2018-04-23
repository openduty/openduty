__author__ = 'deathowl'

from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from .models import Calendar, User, SchedulePolicy, SchedulePolicyRule
from django.contrib.auth.models import Group 
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.contrib import messages


@login_required()
def list(request):
    policies = SchedulePolicy.objects.all()
    return TemplateResponse(request, 'escalation/list.html', {'policies': policies})

@login_required()
def delete(request, id):
    try:
        policy = SchedulePolicy.objects.get(id=id)
        policy.delete()
        return HttpResponseRedirect('/policies/')
    except Calendar.DoesNotExist:
        raise Http404

@login_required()
def new(request):
    try:
        users = User.objects.all()
    except User.DoesNotExist:
        users = None
    try:
        groups = Group.objects.all()
    except Group.DoesNotExist:
        groups = None
    try:
        calendars = Calendar.objects.all()
    except Calendar.DoesNotExist:
        calendars = None

    return TemplateResponse(request, 'escalation/edit.html', {'calendars': calendars, 'groups': groups, 'users': users})

@login_required()
def edit(request, id):
    try:
        policy = SchedulePolicy.objects.get(id=id)
        try:
            elements = SchedulePolicyRule.objects.filter(schedule_policy = policy).order_by('position')
        except SchedulePolicyRule.DoesNotExist:
            elements = None
        try:
            calendars = Calendar.objects.all()
        except Calendar.DoesNotExist:
            calendars = None
        try:
            groups = Group.objects.all()
        except Group.DoesNotExist:
            groups = None
        try:
            users = User.objects.all()
        except User.DoesNotExist:
            users = None

        return TemplateResponse(request, 'escalation/edit.html', {'item': policy, 'elements': elements,
                                                                  'calendars': calendars, 'groups': groups, 'users': users})
    except Calendar.DoesNotExist:
        raise Http404

@login_required()
@require_http_methods(["POST"])
def save(request):
    try:
        policy = SchedulePolicy.objects.get(id=request.POST['id'])
    except SchedulePolicy.DoesNotExist:
        policy = SchedulePolicy()

    policy.name = request.POST['name']
    policy.repeat_times = request.POST['repeat']
    try:
        policy.save()
    except IntegrityError:
        messages.error(request, 'Schedule already exists')
        if int(request.POST['id']) > 0:
            return HttpResponseRedirect(reverse('openduty.escalation.edit', None, [str(request.POST['id'])]))
        else:
            return HttpResponseRedirect(reverse('openduty.escalation.new'))

    elements = request.POST.getlist('escalate_to[]')
    try:
        SchedulePolicyRule.objects.filter(schedule_policy=policy).delete()
    except SchedulePolicyRule.DoesNotExist:
        pass  # Nothing to clear
    for idx,item in enumerate(elements):
        rule = SchedulePolicyRule()
        rule.schedule_policy = policy
        parts = item.split("|")
        rule.escalate_after = 0  # HACK!
        rule.position = idx + 1
        rule.schedule = None
        rule.user_id = None
        rule.group_id = None
        if parts[0] == "user":
            rule.user_id = User.objects.get(id=parts[1])
        elif parts[0] == "calendar":
            rule.schedule = Calendar.objects.get(id=parts[1])
        elif parts[0] == "group":
            rule.group_id = Group.objects.get(id=parts[1])

        try:
            rule.save()
        except IntegrityError:
            return HttpResponseRedirect(reverse('openduty.escalation.edit', None, [str(request.POST['id'])]))


    return HttpResponseRedirect('/policies/')

