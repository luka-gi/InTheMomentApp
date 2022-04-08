"""Accounts view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages

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

class SettingsView(generic.CreateView, MapTemplateView):
    form_class = CustomUserCreationForm
    template_name="settings.html"
    success_url=reverse_lazy('settings')

    def form_valid(self, form):
        Cur_user = self.request.user
        if(form.instance.username == None):
            user.username = form.instance.username
        if(form.instance.email == None):
            user.email = form.instance.email
        if(form.instance.password == None):
            user.password = form.instance.password

        
        return super().form_valid(form)

class BundleView(MapTemplateView):

    model = Bundle
    template_name = 'bundles.html'

    def get_context_data(self, **kwargs):
        userBundles = Bundle.objects.filter(userID = self.request.user)
        context = super().get_context_data(**kwargs)
        context['bundles'] = userBundles
        return context

class CreateBundleView(MapTemplateView):
    template_name="create_bundle.html"
