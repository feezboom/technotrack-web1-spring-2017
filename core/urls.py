from django.conf.urls import url, include

from core.views import show_welcome_page

urlpatterns = [

    url(r'^blogs/', include('blogs.urls', namespace="blogs")),
    url(r'^posts/', include('posts.urls', namespace="posts")),
    url(r'^comments/', include('comments.urls', namespace="comments")),
    url(r'^$', show_welcome_page),

    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('registration.auth_urls')),

    # url(r'^login/', login, {'template_name': 'core/login.html'},
    # name="login"), url(r'^logout/', logout, {'template_name':
    # 'core/logout.html'}, name="logout"),

    # url(r'^test/$', test),
    # url(r'^(\d+)/$', test),

    # url(r'^(?P<blog_id>\d+)/(?P<post_id>\d+)$', test),  # Named argument.
    # url(r'^(?P<post_id>\d+)/$', test),  # Named argument.
]
