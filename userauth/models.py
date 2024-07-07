# userauth/models.py

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from rest_framework import serializers
from uuid import uuid4

# accesstokens
from rest_framework_simplejwt.tokens import RefreshToken

def generate_uuid():
    return uuid4().hex


class User(AbstractBaseUser, PermissionsMixin):
    userId = models.CharField(max_length=255, unique=True, default=generate_uuid)
    firstName = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    email = models.EmailField(_("email"), unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
  
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


#   def save(self, *args, **kwargs):
#         if not self.accessToken:
#             self.accessToken = str(RefreshToken.for_user(self).access_token)
#         super().save(*args, **kwargs)


class Organization(models.Model):
    orgId = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    users = models.ManyToManyField(User, related_name='organizations')

    def __str__(self):
        return self.name
