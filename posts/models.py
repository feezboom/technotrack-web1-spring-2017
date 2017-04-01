from __future__ import unicode_literals

from django.db import models

from core.models import MyAbstractModel


class Post(MyAbstractModel):

    title = models.CharField(max_length=255)
    rate = models.IntegerField()

    def __str__(self):
        return self.title

