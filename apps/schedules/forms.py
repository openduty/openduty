from django import forms
from schedule.models import Calendar


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
