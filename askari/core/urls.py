try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from .views import DashboardView

urlpatterns = patterns('',
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^login/$', 'django.contrib.auth.views.login', {"template_name": 'core/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
