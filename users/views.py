"""Accounts view. """
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, FileResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.http import QueryDict
from django.core.paginator import Paginator
import random



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
        random_number = random.randint(0,16777215) 
        hex_number = str(hex(random_number)) 
        hex_number ='#'+ hex_number[2:] 
        
        form.instance.color = hex_number
        form.save()
        form.instance.bundleID = Bundle.objects.filter(name="Default").get(userID = self.request.user)

        return super().form_valid(form)

class EditReminderView(generic.UpdateView, MapTemplateView):
    model = Reminder
    form_class = EditReminderForm
    template_name ="edit_reminder.html"
    success_url = reverse_lazy('home')
    initial = {}

class DeleteReminderView(generic.DeleteView):
    model = Reminder
    template_name="delete_reminder.html"
    success_url = reverse_lazy('home')

class AcceptShareBundleView(generic.CreateView, MapTemplateView):
    model = ShareBundle
    form_class = EditReminderForm
    template_name ="accept_shareBundle.html"
    success_url = reverse_lazy('bundles')
    initial = {}

class DeleteShareBundleView(generic.DeleteView):
    model = ShareBundle
    template_name="delete_shareBundle.html"
    success_url = reverse_lazy('bundles')

class SettingsView(MapTemplateView):
    template_name="settings.html"

class BundleView(MapTemplateView):

    model = Bundle
    template_name = 'bundles.html'

    def get_context_data(self, **kwargs):
        userBundles = Bundle.objects.filter(userID = self.request.user)
        shareBundles = ShareBundle.objects.filter(receiverID = self.request.user)
        context = super().get_context_data(**kwargs)
        context['bundles'] = userBundles
        context['shareBundles'] = shareBundles
        return context

class CreateBundleView(generic.CreateView, MapTemplateView):
    form_class = BundleForm
    success_url = reverse_lazy('bundles')
    template_name = 'bundle.html'
    

    def form_valid(self, form):
        random_number = random.randint(0,16777215) 
        hex_number = str(hex(random_number)) 
        hex_number ='#'+ hex_number[2:] 
        
        form.instance.color = hex_number
        form.instance.userID = self.request.user
        form.save()
        return super().form_valid(form)

class ShareBundleView(generic.CreateView):
    form_class = ShareBundleForm
    success_url = reverse_lazy('home')
    template_name = 'share_bundle.html'

    def form_valid(self, form):
        form.instance.senderID = self.request.user.email
        form.instance.receiverID = CustomUser.objects.get(email = form.instance.receiverEmail)
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        userBundles = Bundle.objects.filter(userID = self.request.user)
        shareBundles = ShareBundle.objects.all()
        context = super().get_context_data(**kwargs)
        context['bundles'] = userBundles
        context['shareBundles'] = shareBundles
        return context


def AppendReminderView(request):
    context = {
        "bundles": Bundle.objects.filter(userID = request.user),
        "reminders": Reminder.objects.filter(bundleID__userID = request.user)
    }
    

    if request.method == "POST":
        user_chosen_bundle_id = request.POST.get('selectedBundles')
        chosen_bundle = Bundle.objects.get(pk = user_chosen_bundle_id)
        chosen_reminder_id_list = request.POST.getlist('selectedReminders')
        
        
        for reminderID in chosen_reminder_id_list:
            chosen_reminders = Reminder.objects.get(pk = reminderID)
            chosen_reminders.bundleID = chosen_bundle
            chosen_reminders.color = chosen_bundle.color
            chosen_reminders.save()
        

    return render(request, 'append_reminder_bundle.html', context)


