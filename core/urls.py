from django.conf.urls import url

from core.views import test

urlpatterns = [
    url(r'^test/$', test),

    url(r'^(\d+)/$', test),
    url(r'^(?P<blog_id>\d+)/(?P<post_id>\d+)$', test),  # Named argument.
    url(r'^(?P<post_id>\d+)/$', test),  # Named argument.
]
