try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here
from askari.databases.views import DatabaseCreateView

urlpatterns = patterns('',
    url(r'^new/', DatabaseCreateView.as_view(), name='test')
)
