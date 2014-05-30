try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here
from .views import DatabaseCreateView, DatabaseListView

urlpatterns = patterns('',
    url(r'^new/', DatabaseCreateView.as_view(), name='new'),
    url(r'^$', DatabaseListView.as_view(), name='list')
)
