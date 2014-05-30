try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here
from .views import (DatabaseCreateView, DatabaseListView, DatabaseUpdateView,
    DatabaseDeleteView,)

urlpatterns = patterns('',
    url(r'^new/', DatabaseCreateView.as_view(), name='new'),
    url(r'^(?P<pk>[\d]+)/edit$', DatabaseUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>[\d]+)/delete$', DatabaseDeleteView.as_view(), name='delete'),
    url(r'^$', DatabaseListView.as_view(), name='list')
)
