import uuid
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth import get_user_model

User = get_user_model()


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


class SignUpPatientForm(forms.ModelForm):

    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'required': 'required', 'placeholder': 'First Name'}
        )
    )
    last_name = forms.CharField(
        required=True,
        label= 'Last Name',
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'required': 'required', 'placeholder': 'Last Name'}
        )
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={'type': 'email', 'class': "form-control", 'required': 'required', 'placeholder': 'Email'}
        )
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'required': 'required', 'placeholder': 'Username'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'type': 'password', 'class': "form-control", 'required': 'required', 'placeholder': 'Password'}
        ),

    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password', 'class': "form-control", 'required': 'required',
                'placeholder': 'Password confirmation'
            }
        ),
    )

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.exclude(id=self.instance.id).get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError("This email address is already in use. Please supply a different email address.")

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.instance)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.instance.save(commit=False)
        self.instance.set_password(password)
        if commit:
            self.instance.save()
        return self.instance

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'password2']
