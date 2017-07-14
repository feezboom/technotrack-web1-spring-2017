from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from comments.forms import CreateCommentForm
from core.views import test
from posts.views import PostView, CreatePost

urlpatterns = [
    url(r'^$', login_required(test), name="all_posts"),
    # todo : make comment creation correct
    url(r'^(?P<pk>\d+)/$', login_required(PostView.as_view()),
        kwargs={'form': CreateCommentForm()},
        name="show_post_by_id"),
    url(r'^create_post', login_required(CreatePost.as_view()),
        name="create_post")
]
