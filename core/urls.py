from django.conf.urls import url, include
from registration.views import RegistrationView

from core.models import User
from core.views import show_welcome_page

urlpatterns = [

    url(r'^blogs/', include('blogs.urls', namespace="blogs")),
    url(r'^posts/', include('posts.urls', namespace="posts")),
    url(r'^comments/', include('comments.urls', namespace="comments")),
    url(r'^$', show_welcome_page, name="welcome_page"),

    url(r'^accounts/register/$',
        RegistrationView.as_view(form_class=User),
        name='registration_register'),

    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('registration.auth_urls')),

]
