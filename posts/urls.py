from django.conf.urls import url

from core.views import test
from posts.views import PostView

urlpatterns = [
    url(r'^$', test, name="all_posts"),
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name="show_post_by_id"),
]
