from __future__ import unicode_literals

from django.db import models

from core.models import MyAbstractModel
from posts.models import Post


class Comment(MyAbstractModel):

    post_owner = models.ForeignKey(Post, default=None)
    text = models.TextField(default=None)

    def __str__(self):
        return "Author : " + str(self.author)
