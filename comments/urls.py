from django.conf.urls import url

from core.views import test

urlpatterns = [
    url(r'^$', test),
    url(r'^(?P<comment_id>\d+)$', test),

]
