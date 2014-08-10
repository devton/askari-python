from django.conf.urls import patterns, include, url
from .views import DashboardView

urlpatterns = patterns(
    '',
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),

    url(r'^databases/', include('askari.databases.urls', 
                                namespace="databases")),
    url(r'^dataclips/', include('askari.dataclips.urls', 
                                namespace="dataclips")),
)
