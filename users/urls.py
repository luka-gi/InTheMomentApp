"""Accounts app URL Configuration."""
from django.urls import path
from .views import *
from users import views

app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
