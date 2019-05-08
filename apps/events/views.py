from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from schedule.models import Calendar
from schedule.views import CreateEventView, EditEventView, EventMixin
from apps.events.forms import CustomEventForm


class CustomCreateEventView(CreateEventView):
    form_class = CustomEventForm
    template_name = 'event/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CustomCreateEventView, self).get_context_data(**kwargs)
        calendar = get_object_or_404(Calendar, slug=self.kwargs.get('calendar_slug'))
        extra_context = {
            "calendar": calendar,
        }
        context.update(extra_context)
        return context

    def form_valid(self, form):
        super(CustomCreateEventView, self).form_valid(form)
        messages.error(self.request, 'Event created successfully.')
        return HttpResponseRedirect(
            reverse('calendar_details', kwargs={'calendar_slug': self.kwargs.get('calendar_slug')})
        )


class CustomUpdateEventView(EditEventView):
    form_class = CustomEventForm
    template_name = 'event/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CustomUpdateEventView, self).get_context_data(**kwargs)
        calendar = get_object_or_404(Calendar, slug=self.kwargs.get('calendar_slug'))
        extra_context = {
            "calendar": calendar,
        }
        context.update(extra_context)
        return context

    def form_valid(self, form):
        super(CustomUpdateEventView, self).form_valid(form)
        messages.error(self.request, 'Event edited successfully.')
        return HttpResponseRedirect(
            reverse('calendar_details', kwargs={'calendar_slug': self.kwargs.get('calendar_slug')})
        )


class CustomDeleteEventView(LoginRequiredMixin, EventMixin, DeleteView):
    """Delete Event"""
    template_name = 'event/delete.html'

    def get_success_url(self):
        return reverse('calendar_details', args=[self.kwargs.get('calendar_slug')])

    def get_context_data(self, **kwargs):
        context = super(CustomDeleteEventView, self).get_context_data(**kwargs)
        calendar = get_object_or_404(Calendar, slug=self.kwargs.get('calendar_slug'))
        context.update(
            {
                'event': self.object,
                'calendar': calendar
            }
        )
        return context
