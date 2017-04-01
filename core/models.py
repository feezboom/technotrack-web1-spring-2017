from django.db import models
from django.contrib.auth.models import AbstractUser

from MySocialNetwork import settings


class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)


class MyAbstractModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
