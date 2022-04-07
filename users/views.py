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
        form.instance.bundleID = Bundle.objects.filter(name="Default").get(userID = self.request.user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        userBundles = Bundle.objects.get(userID = self.request.user)
        context = super().get_context_data(**kwargs)
        context['reminders'] = Reminder.objects.filter(bundleID=userBundles)
        return context

class MapTemplateView(LoginRequiredMixin, generic.ListView):

    model = Reminder

    def get_context_data(self, **kwargs):
        userBundles = Bundle.objects.get(userID = self.request.user)
        context = super().get_context_data(**kwargs)
        context['reminders'] = Reminder.objects.filter(bundleID=userBundles)
        return context
