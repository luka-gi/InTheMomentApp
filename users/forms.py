"""Forms for accounts app."""
from django import forms
from .models import CustomUser, Bundle, Reminder
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)


class CustomUserCreationForm(UserCreationForm):
    """Registration form."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = ("first_name", "last_name", "email", "password1", "password2")
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.TextInput(attrs={"class": "form-control"}),
            'password2': forms.TextInput(attrs={"class": "form-control"}),
        }


class CustomUserChangeForm(UserChangeForm):
    """User profile change view."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = ('email',)


class ReminderForm(forms.ModelForm):

    class Meta:
        model = Reminder
        fields = ('name', 'body', 'location',)
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.TextInput(attrs={"class": "form-control"}),
            'location': forms.TextInput(attrs={"class": "form-control"}),
        }


