from django.conf.urls import url

from blogs.views import BlogsList, BlogView

urlpatterns = [
    url(r'^$', BlogsList.as_view(), name="show_all_blogs"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="show_blog_by_id"),
]
