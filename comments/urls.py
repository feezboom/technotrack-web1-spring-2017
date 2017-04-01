from django.conf.urls import url

from core.views import test

urlpatterns = [
    url(r'^$', test, name="comments_root"),
    url(r'^(?P<comment_id>\d+)$', test),
]
