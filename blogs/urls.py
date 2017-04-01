from django.conf.urls import url

from blogs.views import show_all_blogs, show_one_blog

urlpatterns = [
    url(r'^$', show_all_blogs, name="show_all_blogs"),
    url(r'^(?P<blog_id>\d+)/$', show_one_blog, name="show_one_blog"),
]
