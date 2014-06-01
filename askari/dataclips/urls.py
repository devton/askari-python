try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from .views import ClipCreateView, ClipUpdateView, ClipDeleteView, ClipListView, ClipPublicView


urlpatterns = patterns('',
    url(r'^$', ClipListView.as_view(), name='list'),
    url(r'^new/', ClipCreateView.as_view(), name='new'),
    url(r'^(?P<pk>[\d]+)$', ClipUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>[\d]+)/public$', ClipPublicView.as_view(), name='public'),
    url(r'^(?P<pk>[\d]+)/delete$', ClipDeleteView.as_view(), name='delete'),
    #url(r'^(?P<pk>[\d]+)/edit$', DatabaseUpdateView.as_view(), name='edit'),
    #url(r'^(?P<pk>[\d]+)/delete$', DatabaseDeleteView.as_view(), name='delete'),
    #url(r'^$', DatabaseListView.as_view(), name='list')
)

