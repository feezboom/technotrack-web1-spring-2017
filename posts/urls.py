from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from core.views import test
from posts.views import PostView

urlpatterns = [
    url(r'^$', login_required(test), name="all_posts"),
    url(r'^(?P<pk>\d+)/$', login_required(PostView.as_view()), name="show_post_by_id"),
]
