from django.conf.urls import url

from blogs.views import show_all_blogs
from core.views import test

urlpatterns = [
    url(r'^$', show_all_blogs),
    url(r'^(?P<comment_id>\d+)$', test, name="show_comment_by_id"),
]
