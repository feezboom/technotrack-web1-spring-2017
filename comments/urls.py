from django.conf.urls import url

from blogs.views import BlogsList
from core.views import test

urlpatterns = [
    url(r'^$', BlogsList.as_view()),
    url(r'^(?P<pk>\d+)$', test, name="show_comment_by_id"),
]
