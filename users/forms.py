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
        fields = ('name', 'body', 'location', 'bundleID')
        widgets = {
            'bundleID': forms.IntegerField(),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.TextInput(attrs={"class": "form-control"}),
            'location': forms.TextInput(attrs={"class": "form-control"}),
        }

class BundleForm(forms.ModelForm):

    class Meta:
        model = Bundle
        fields = {'name'}
        widgets = {
            'name': forms.TextInput({"class": "form-control"})
        }

class AppendReminderForm(forms.Form):
    selectedBundles = forms.ModelChoiceField(queryset=None)
    selectedReminders = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
         """ Grants access to the request object so that only bundles and reminders created by the current user is displayed in the form. """
         self.request = kwargs.pop('request')
         super().__init__()

        # Get all user bundles created by the current user
         user_bundles = Bundle.objects.filter(userID=self.request.user)
         self.fields['selectedBundles'].queryset = user_bundles
        
        # Get all reminders created by the current user
         user_reminders = Reminder.objects.filter(bundleID = user_bundles)

         self.fields['selectedBundles'].queryset = user_reminders
         super().__init__()


