from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from blogs.views import BlogsList, BlogView, CreateBlog
from posts.views import CreatePost

urlpatterns = [
    url(r'^$', login_required(BlogsList.as_view()), name="show_all_blogs"),
    url(r'^(?P<pk>\d+)/$', login_required(BlogView.as_view()),
        name="show_blog_by_id"),
    url(r'^create_blog', login_required(CreateBlog.as_view()),
        name="create_blog")

]
