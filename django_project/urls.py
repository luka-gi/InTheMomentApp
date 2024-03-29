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
from users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('bundles',BundleView.as_view(),name="bundles"),
    path('settings',SettingsView.as_view(),name="settings"),
    path('create_bundle',CreateBundleView.as_view(),name= 'create_bundle'),
    path('create_reminder', CreateReminderView.as_view(), name='create_reminder'),
    path('testing',
        MapTemplateView.as_view(template_name="testing.html"),
        name="testing"),
    path('append_reminder_bundle', AppendReminderView, name = 'append_reminder_bundle'),
    path('share_bundle', ShareBundleView.as_view(), name='share_bundle'),
    path('accept_shareBundle/<slug:pk>/', AcceptShareBundleView.as_view(), name='accept_shareBundle'),
    path('delete_shareBundle/<slug:pk>/', DeleteShareBundleView.as_view(), name='delete_shareBundle'),
    path('edit_reminder/<slug:pk>/', EditReminderView.as_view(), name='edit_reminder'),
    path('delete_reminder/<slug:pk>', DeleteReminderView.as_view(), name='delete_reminder'),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

