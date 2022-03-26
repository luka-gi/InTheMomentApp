"""django_project URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

Examples
--------
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',
         TemplateView.as_view(template_name="home.html"),
         name="home"),
    path('bundle_sidebar',
         TemplateView.as_view(template_name="bundle_sidebar.html"),
         name="bundle_sidebar"),
    path('testing',
         TemplateView.as_view(template_name="testing.html"),
         name="testing"),
    path('settings',
         TemplateView.as_view(template_name="settings.html"),
         name="settings"),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Create_Pin_Sidebar',
         TemplateView.as_view(template_name="Create-Pin-Sidebar.html"),
         name="Create_Pin_Sidebar"),
]

urlpatterns += staticfiles_urlpatterns()
