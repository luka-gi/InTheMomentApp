"""Accounts models."""
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.forms import ImageField
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class CustomUser(AbstractUser):
    """Custom User class."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """Return email as the object's string representation."""
        return self.email


class Bundle(models.Model):

    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    color = models.TextField(max_length = 10)

    objects = models.Manager()

    def __int__(self):
        return self.id

@receiver(post_save, sender=CustomUser)
def create_bundle(sender, instance, created, **kwargs):
    if created:
        Bundle.objects.create(userID=instance, name = "Default")


class Reminder(models.Model):

    bundleID = models.ForeignKey(Bundle, null=True, blank=True, on_delete=models.CASCADE)
    name = models.TextField(max_length=200)
    body = models.TextField(max_length=500)
    location = models.TextField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    paused = models.BooleanField(default=False)
    alertTime = models.DateTimeField(auto_now=False, null=True, blank=True)
    color = models.TextField(max_length = 10)

    objects = models.Manager()
    
    def __str__(self):
        return self.name


class ShareBundle(models.Model):

    senderID = models.TextField(max_length=200)
    receiverEmail = models.TextField(max_length=200)
    receiverID = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    shareBundle = models.TextField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return self.shareBundle
    
