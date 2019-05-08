import datetime
from django.utils import timezone
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group, User
from schedule.models import Event, Rule
from schedule.forms import EventForm
from schedule.widgets import ColorInput


class CustomEventForm(EventForm):
    def __init__(self, *args, **kwargs):
        super(CustomEventForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['start_0'].initial = timezone.localtime(self.instance.start).date()
            self.fields['start_1'].initial = timezone.localtime(self.instance.start).time().strftime("%H:%M")
            self.fields['end_0'].initial = timezone.localtime(self.instance.end).date()
            self.fields['end_1'].initial = timezone.localtime(self.instance.end).time().strftime("%H:%M")
            on_call_list = self.instance.title.split(',') if self.instance.title.split(',') != [''] else ["", ""]
            if on_call_list:
                self.fields['on_call'].initial = on_call_list[0]
                self.fields['fallback'].initial = on_call_list[1]

    on_call_choices = [
        ("", "-----"),
        ('Groups', [(x.name, x.name) for x in Group.objects.all()]),
        ('People', [(x.username, x.username) for x in User.objects.all()])
    ]

    start_0 = forms.DateField(
        label=_("start"),
        required=True,
        widget=forms.DateInput(
            attrs={'type': 'text', 'class': "form-control datepicker"}
        )
    )
    start_1 = forms.TimeField(
        label=_("start"),
        required=True,
        widget=forms.TimeInput(
            attrs={'type': 'text', 'class': "form-control"}
        )
    )
    end_0 = forms.DateField(
        label=_("start"),
        required=True,
        widget=forms.DateInput(
            attrs={'type': 'text', 'class': "form-control datepicker"}
        )
    )
    end_1 = forms.TimeField(
        label=_("End Time"),
        required=True,
        help_text=_("The end time must be later than start time."),
        widget=forms.TimeInput(
            attrs={'type': 'text', 'class': "form-control"}
        )
    )
    end_recurring_period = forms.DateTimeField(
        label=_("End recurring"),
        help_text=_("This date is ignored for one time only events."),
        required=False,
        widget=forms.DateInput(
            attrs={'type': 'text', 'class': "form-control datepicker"}
        )
    )
    description = forms.CharField(
        label=_("Description"),
        required=False,
        widget=forms.Textarea(
            attrs={'type': 'text', 'class': "form-control", "rows": 5, "cols": 40}
        )
    )
    color_event = forms.CharField(
        label=_('Event Color'),
        required=True,
        widget=ColorInput(
            attrs={'class': "form-control", "style": "width: 75px;padding: 0;"}
        )
    )
    on_call = forms.ChoiceField(
        required=False,
        label=_('On Call'),
        choices=on_call_choices,
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )
    fallback = forms.ChoiceField(
        required=False,
        label=_('Fallback'),
        choices=on_call_choices,
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )
    rule = forms.ModelChoiceField(
        required=False,
        help_text=_("Select '----' for a one time only event."),
        label=_('Recurring'),
        queryset=Rule.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = Event
        fields = [
            'start_0', 'start_1', 'end_0', 'end_1',
            'description', 'rule', 'on_call', 'fallback'
        ]

    def save(self, commit=True):
        instance = super(CustomEventForm, self).save(commit=False)
        instance.start = timezone.make_aware(datetime.datetime.combine(
            self.cleaned_data['start_0'], self.cleaned_data['start_1']
        ))
        instance.end = timezone.make_aware(datetime.datetime.combine(
            self.cleaned_data['end_0'], self.cleaned_data['end_1']
        ))
        if instance.end <= instance.start:
            raise forms.ValidationError(_("The end time must be later than start time."))
        instance.title = ','.join([self.cleaned_data['on_call'], self.cleaned_data['fallback']])
        return instance
