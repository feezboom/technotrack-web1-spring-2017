from django.conf.urls import url

from core.views import test
from posts.views import show_post

urlpatterns = [
    url(r'^$', test, name="all_posts"),
    url(r'^(?P<post_id>\d+)/$', show_post, name="post_by_id"),
]
