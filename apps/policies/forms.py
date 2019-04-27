from django import forms
from apps.policies.models import SchedulePolicy


class SchedulePolicyForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label='Policy name',
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'required': 'required', 'placeholder': 'Policy name'}
        )
    )
    repeat_times = forms.CharField(
        required=True,
        label='Repeat',
        widget=forms.NumberInput(
            attrs={'type': 'number', 'class': "form-control", 'required': 'required', 'placeholder': 'Repeat x times'}
        )
    )

    class Meta:
        model = SchedulePolicy
        fields = (
            'name',
            'repeat_times'
        )
