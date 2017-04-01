from __future__ import unicode_literals

from django.db import models

from core.models import MyAbstractModel
from posts.models import Post


class Comment(MyAbstractModel):

    post_owner = models.ForeignKey(Post, default=None)

    def __str__(self):
        return "Author : " + self.author
