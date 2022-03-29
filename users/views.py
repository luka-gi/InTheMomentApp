"""Accounts view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages


class SignUpView(generic.CreateView):
    """Registration view."""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CreateReminderView(LoginRequiredMixin, generic.CreateView):

    form_class = ReminderForm
    success_url = reverse_lazy('home')
    template_name = 'create_reminder.html'

    def form_valid(self, form):
        self.object = form.save()
        currentUser = self.request.user
        defaultBundle = Bundle.objects.filter(userID=currentUser).get(name="Default")
        self.object.bundleID = defaultBundle
        return HttpResponseRedirect(self.get_success_url())
