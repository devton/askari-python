from django.conf.urls import patterns, include, url
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'askari.views.home', name='home'),
    # url(r'^askari/', include('askari.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^databases/', include('askari.databases.urls', namespace="databases")),
    url(r'^dataclips/', include('askari.dataclips.urls', namespace="dataclips")),
    url(r'^', include('askari.core.urls', namespace="core")),
)
