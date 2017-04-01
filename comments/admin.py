from django.contrib import admin

from blogs.models import Blog
from comments.models import Comment
from posts.models import Post

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Comment)
