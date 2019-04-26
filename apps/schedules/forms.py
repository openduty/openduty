from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from schedule.models import Calendar
from apps.notification.notifier.hipchat import HipchatNotifier


class CalendarForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label='Name',
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'required': 'required', 'placeholder': 'Schedule Name'}
        )
    )
    slug = forms.CharField(
        required=True,
        label='Slug',
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'required': 'required', 'placeholder': 'Slug'}
        )
    )

    class Meta:
        model = Calendar
        fields = (
            'name',
            'slug'
        )
