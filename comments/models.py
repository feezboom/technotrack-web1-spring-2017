from __future__ import unicode_literals

from django.db import models

from core.models import MyAbstractModel


class Comment(MyAbstractModel):

    def __str__(self):
        return "Author : " + self.author
