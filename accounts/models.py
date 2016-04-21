from django.db import models
from django import forms
# Create your models here.
from django.conf import settings


class UserProfile(models.Model):
    #usuario
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #password
    password = models.CharField(max_length=12)
    #email de registro
    email =  models.CharField(max_length=255)
