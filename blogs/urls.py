from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from blogs.views import BlogsList, BlogView

urlpatterns = [
    url(r'^$', login_required(BlogsList.as_view()), name="show_all_blogs"),
    url(r'^(?P<pk>\d+)/$', login_required(BlogView.as_view()),
        name="show_blog_by_id"),
]
