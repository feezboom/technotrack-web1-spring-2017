from __future__ import unicode_literals

from django.db import models

from core.models import MyAbstractModel


class Blog(MyAbstractModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()

    def __str__(self):
        return str(self.title)
