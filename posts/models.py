from __future__ import unicode_literals

from django.db import models

from blogs.models import Blog
from core.models import MyAbstractModel


class Post(MyAbstractModel):

    title = models.CharField(max_length=255)
    text = models.TextField(default=None)
    rate = models.IntegerField()

    blog_owner = models.ForeignKey(Blog, default=None)

    def __str__(self):
        return str(self.title)

