try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

# place app url patterns here
from .views import DatabaseCreateView, DatabaseListView, DatabaseUpdateView

urlpatterns = patterns('',
    url(r'^new/', DatabaseCreateView.as_view(), name='new'),
    url(r'^edit/(?P<object_id>[\d]+)$', DatabaseUpdateView.as_view(), name='edit'),
    url(r'^$', DatabaseListView.as_view(), name='list')
)
