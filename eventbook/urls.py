from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'', include('querying.urls')),
    url(r'^mine/', include('mining.urls')),
    url(r'^cluster/', include('clustering.urls')),
    url(r'^admin/', include(admin.site.urls)),
]