import pytz
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.utils.datetime_safe import datetime
from django.utils import timezone
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from apps.incidents import escalation_helper
from schedule.models import Calendar
from schedule.periods import Month, Year
from schedule.utils import coerce_date_dict
from schedule.periods import weekday_abbrs, weekday_names


@login_required()
def list(request):
    schedules = Calendar.objects.all()
    return TemplateResponse(request, 'schedules/list.html', {'schedules': schedules})


@login_required()
def delete(request, calendar_slug):
    try:
        sched = get_object_or_404(Calendar, slug=calendar_slug)
        sched.delete()
        return HttpResponseRedirect('/schedules/')
    except Calendar.DoesNotExist:
        raise Http404


@login_required()
def new(request):
    try:
        return TemplateResponse(request, 'schedules/edit.html', {})
    except Calendar.DoesNotExist:
        raise Http404


@login_required()
def details(request, calendar_slug,  periods=None):
    try:
        schedule = get_object_or_404(Calendar, slug=calendar_slug)
        date = coerce_date_dict(request.GET) or None
        if date:
            try:
                date = datetime(**date)
            except ValueError:
                raise Http404
        else:
            date = timezone.now()
        event_list = schedule.event_set.all()
        currently_oncall_users = escalation_helper.get_current_events_users(schedule)
        if len(currently_oncall_users) >= 2:
            oncall1 = f"{currently_oncall_users[0].username}, Phone Number: {currently_oncall_users[0].profile.phone_number}"
            oncall2 = f"{currently_oncall_users[1].username}, Phone Number: {currently_oncall_users[1].profile.phone_number}"
        else:
            oncall1 = "Nobody"
            oncall2 = "Nobody"

        if 'django_timezone' in request.session:
            local_timezone = pytz.timezone(request.session['django_timezone'])
        else:
            local_timezone = timezone.get_default_timezone()
        period_objects = {}
        for period in periods:
            if period.__name__.lower() == 'year':
                period_objects[period.__name__.lower()] = Year(event_list, date, None, local_timezone)
            else:
                period_objects[period.__name__.lower()] = Month(event_list, date, None, None, local_timezone)
        template = 'schedules/detail.html'
        month = period_objects['month']
        shift = None
        if shift:
            if shift == -1:
                month = month.prev()
            if shift == 1:
                month = next(month)
        size = 'regular'
        if size == 'small':
            day_names = weekday_abbrs
        else:
            day_names = weekday_names

        context = {
            'day_names': day_names,
            'month': month,
            'size': size,

            'date': date,
            'periods': period_objects,
            'calendar': schedule,
            'weekday_names': weekday_names,
            'currently_oncall_1': oncall1,
            'currently_oncall_2': oncall2,
            'local_timezone': local_timezone,
            'current_date': timezone.now(),
            'here': f"{request.get_full_path()}",
        }
        return render(request, template, context)
    except Calendar.DoesNotExist:
        raise Http404


@login_required()
def edit(request, calendar_slug):
    try:
        sched = get_object_or_404(Calendar, slug=calendar_slug)
        return TemplateResponse(request, 'schedules/edit.html', {'item': sched, 'edit': True})
    except Calendar.DoesNotExist:
        raise Http404


@login_required()
@require_http_methods(["POST"])
def save(request):
    try:
        sched = Calendar.objects.get(slug=request.POST['slug'])
    except Calendar.DoesNotExist:
        sched = Calendar()

    sched.name = request.POST['name']
    sched.slug = request.POST['slug']
    try:
        sched.save()
        return HttpResponseRedirect('/schedules/')
    except IntegrityError:
        messages.error(request, 'Schedule already exists')
        if request.POST['slug']:
            return HttpResponseRedirect(reverse('openduty.schedules.edit', None, [request.POST['slug']]))
        else:
            return HttpResponseRedirect(reverse('openduty.schedules.new'))
