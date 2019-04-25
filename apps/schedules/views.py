import pytz
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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
from schedule.views import FullCalendarView, CalendarMixin
from schedule.periods import Month, Year
from schedule.utils import coerce_date_dict
from schedule.periods import weekday_abbrs, weekday_names


class SchedulesListView(LoginRequiredMixin, ListView):
    model = Calendar
    template_name = 'schedules/list.html'
    context_object_name = 'schedules'


@login_required()
def delete(request, calendar_slug):
    try:
        sched = get_object_or_404(Calendar, slug=calendar_slug)
        sched.delete()
        return HttpResponseRedirect('/schedules/')
    except Calendar.DoesNotExist:
        raise Http404



class SchedulesDetailView(LoginRequiredMixin, CalendarMixin, DetailView):
    model = Calendar
    slug_url_kwarg = 'calendar_slug'
    template_name = 'schedules/detail.html'
    context_object_name = 'schedules'

    def get_on_call_users(self):
        schedule = self.get_object()
        currently_on_call_users = escalation_helper.get_current_events_users(schedule)
        on_call_1, on_call_2 = "Nobody", "Nobody"
        if len(currently_on_call_users) >= 2:
            user_1, user_2 = currently_on_call_users[0], currently_on_call_users[1]
            on_call_1 = f"{user_1.username}, Phone Number: {user_1.profile.phone_number}"
            on_call_2 = f"{user_2.username}, Phone Number: {user_2.profile.phone_number}"
        return on_call_1, on_call_2

    def get_context_data(self, **kwargs):
        context = super(SchedulesDetailView, self).get_context_data(**kwargs)
        schedule = self.get_object()
        date = timezone.now()
        date_from_request = coerce_date_dict(self.request.GET) or None
        if date_from_request:
            try:
                date = datetime(**date_from_request)
            except ValueError:
                raise Http404
        event_list = schedule.event_set.all()
        on_call_1, on_call_2 = self.get_on_call_users()
        local_timezone = timezone.get_default_timezone()
        if 'django_timezone' in self.request.session:
            local_timezone = pytz.timezone(self.request.session['django_timezone'])
        period_objects = {}
        for period in [Month]:
            if period.__name__.lower() == 'year':
                period_objects[period.__name__.lower()] = Year(event_list, date, None, local_timezone)
            else:
                period_objects[period.__name__.lower()] = Month(event_list, date, None, None, local_timezone)

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

        extra_context = {
            'day_names': day_names,
            'month': month,
            'size': size,
            'date': date,
            'periods': period_objects,
            'calendar': schedule,
            'weekday_names': weekday_names,
            'currently_oncall_1': on_call_1,
            'currently_oncall_2': on_call_2,
            'local_timezone': local_timezone,
            'current_date': timezone.now(),
            'here': f"{self.request.get_full_path()}",
        }
        context.update(extra_context)
        return context


@login_required()
def new(request):
    try:
        return TemplateResponse(request, 'schedules/edit.html', {})
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
