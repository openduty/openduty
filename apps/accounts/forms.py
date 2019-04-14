from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from apps.accounts.models import Profile
from betterforms.multiform import MultiModelForm
from apps.notification.notifier.hipchat import HipchatNotifier


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'required': 'required', 'placeholder': 'Username'}
        )
    )
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.TextInput(
            attrs={'type': 'password', 'class': "form-control", 'required': 'required', 'placeholder': 'Password'}
        )
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={'type': 'email', 'class': "form-control", 'required': 'required', 'placeholder': 'Email'}
        )
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'type': 'password', 'class': "form-control", 'required': 'required', 'placeholder': 'New password'}
        ),

    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password', 'class': "form-control", 'required': 'required',
                'placeholder': 'New password confirmation'
            }
        ),
    )


class UserForm(forms.ModelForm):
    """Django default User Form"""
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )


class ProfileForm(forms.ModelForm):
    """User Profile Form"""
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        hipchat_room_name = self.fields.get('hipchat_room_name')
        hipchat_rooms = HipchatNotifier(settings.HIPCHAT_SETTINGS).get_all_rooms()
        if hipchat_rooms:  # pragma: no cover
            hipchat_room_name.choices = list(hipchat_room_name.choices) + hipchat_rooms
        else:
            hipchat_room_name.choices = list(hipchat_room_name.choices) + \
                                        [("", ""), ("room", "Room")]

    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "+44"})
    )
    pushover_user_key = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    pushover_app_key = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    slack_room_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    prowl_api_key = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    prowl_application = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    prowl_url = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    rocket_webhook_url = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    hipchat_room_name = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    hipchat_room_url = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    send_resolve_enabled = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'flat-red'})
    )

    class Meta:
        model = Profile
        fields = (
            'phone_number',
            'pushover_user_key',
            'pushover_app_key',
            'slack_room_name',
            'prowl_api_key',
            'prowl_application',
            'prowl_url',
            'rocket_webhook_url',
            'hipchat_room_name',
            'hipchat_room_url',
            'send_resolve_enabled'
        )


class UserProfileMultiForm(MultiModelForm):
    """MultiForm for Users and Profile"""

    form_classes = {
        'user': UserForm,
        'profile': ProfileForm,
    }
