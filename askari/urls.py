from django.conf.urls import patterns, include, url
from django.contrib import admin

from .core.views import UserRegistrationView, UserLoginView


# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', 
                     {"template_name": 'core/login.html'}, 
                     name='login'),

    url(r'^register/$', UserRegistrationView.as_view(), name='registration'),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', 
                      name='logout'),

    url(r'^success_login/$', UserLoginView.as_view(), name='login_redirect'),
    url(r'^(?P<organization>\w+)/', include('askari.core.urls')),
)
