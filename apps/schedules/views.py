import pytz
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.datetime_safe import datetime
from django.utils import timezone
from django.http import Http404
from apps.incidents import escalation_helper
from apps.schedules.forms import CalendarForm
from schedule.models import Calendar
from schedule.views import CalendarMixin
from schedule.periods import Month
from schedule.utils import coerce_date_dict
from schedule.periods import weekday_abbrs, weekday_names


class SchedulesListView(LoginRequiredMixin, ListView):
    model = Calendar
    template_name = 'schedules/list.html'
    context_object_name = 'schedules'


class SchedulesDeleteView(LoginRequiredMixin, CalendarMixin, DeleteView):
    """Delete Schedules"""
    success_url = '/schedules/'


class SchedulesDetailView(LoginRequiredMixin, CalendarMixin, DetailView):
    template_name = 'schedules/detail.html'
    context_object_name = 'item'

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
        if 'django_timezone' in self.request.session:  # pragma: no cover
            local_timezone = pytz.timezone(self.request.session['django_timezone'])
        period_objects = {}
        month = Month(event_list, date, None, None, local_timezone)
        shift = None
        if shift:  # pragma: no cover
            if shift == -1:
                month = month.prev()
            if shift == 1:
                month = month.next()
        size = 'regular'
        day_names = weekday_abbrs if size == 'small' else weekday_names

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


class SchedulesCreateView(LoginRequiredMixin, CalendarMixin, CreateView):
    template_name = 'schedules/edit.html'
    context_object_name = 'item'
    form_class = CalendarForm
    success_url = '/schedules/'


class SchedulesUpdateView(LoginRequiredMixin, CalendarMixin, UpdateView):
    template_name = 'schedules/edit.html'
    context_object_name = 'item'
    form_class = CalendarForm
    success_url = '/schedules/'
