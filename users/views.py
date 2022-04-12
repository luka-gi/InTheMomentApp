"""Accounts view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.http import QueryDict


class MapTemplateView(LoginRequiredMixin, generic.ListView):

    model = Reminder
    template_name="base_generic.html"

    def get_context_data(self, **kwargs):
        userBundles = Bundle.objects.filter(userID = self.request.user)
        context = super().get_context_data(**kwargs)
        context['reminders'] = Reminder.objects.filter(bundleID__in=userBundles)
        return context

class SignUpView(generic.CreateView):
    """Registration view."""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class HomeView(MapTemplateView):
    template_name = 'home.html'

class CreateReminderView(generic.CreateView, MapTemplateView):

    form_class = ReminderForm
    success_url = reverse_lazy('home')
    template_name = 'create_reminder.html'

    def form_valid(self, form):
        form.instance.bundleID = Bundle.objects.filter(name="Default").get(userID = self.request.user)
        return super().form_valid(form)

class SettingsView(MapTemplateView):
    template_name="settings.html"

class BundleView(MapTemplateView):

    model = Bundle
    template_name = 'bundles.html'

    def get_context_data(self, **kwargs):
        userBundles = Bundle.objects.filter(userID = self.request.user)
        context = super().get_context_data(**kwargs)
        context['bundles'] = userBundles
        return context

class CreateBundleView(generic.CreateView, MapTemplateView):
    form_class = BundleForm
    success_url = reverse_lazy('home')
    template_name = 'bundle.html'
    

    def form_valid(self, form):
        form.instance.userID = self.request.user
        form.save()
        return super().form_valid(form)

class AppendReminderView(generic.CreateView, MapTemplateView):
    form_class = ReminderForm
    success_url = reverse_lazy('home')
    template_name = 'append_reminder_bundle.html'

    def form_valid(self, form):
        userBundle = Bundle.objects.filter(name = 'name')
        form.instance.bundleID = bundle_id
        return super().form_valid(form)