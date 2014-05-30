try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from .views import ClipCreateView, ClipDetailView


urlpatterns = patterns('',
    url(r'^new/', ClipCreateView.as_view(), name='new'),
    url(r'^(?P<pk>[\d]+)$', ClipDetailView.as_view(), name='show'),
    #url(r'^(?P<pk>[\d]+)/edit$', DatabaseUpdateView.as_view(), name='edit'),
    #url(r'^(?P<pk>[\d]+)/delete$', DatabaseDeleteView.as_view(), name='delete'),
    #url(r'^$', DatabaseListView.as_view(), name='list')
)
