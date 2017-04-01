from django.conf.urls import url

from blogs.views import show_blogs, show_blog

urlpatterns = [
    url(r'^$', show_blogs, name="show_all_blogs"),
    url(r'^(?P<blog_id>\d+)/$', show_blog, name="show_one_blog"),
]
