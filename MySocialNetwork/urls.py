"""my_social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from core.views import test

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^test/$', test),

    # url(r'^posts/(\d+)/$', test),
    # url(r'^blogs/(?P<blog_id>\d+)/(?P<post_id>\d+)$', test),# Named argument.

    # url(r'^posts/(?P<post_id>\d+)/$', test),  # Named argument.

    url(r'^core/', include('core.urls')),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^comments/', include('comments.urls')),
]
