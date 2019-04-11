from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm

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
