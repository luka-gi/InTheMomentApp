"""Admin views."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (CustomUserCreationForm, CustomUserChangeForm)
from .models import *


class CustomUserAdmin(UserAdmin):
    """Custom User admin view."""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (
            None,
            {
                'fields': ('email', 'password')
            }
        ),
        (
            'Permissions',
            {
                'fields': ('is_staff', 'is_active')
            }
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2',
                           'is_staff', 'is_active')
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Bundle)
admin.site.register(Reminder)
admin.site.register(ShareBundle)