from django.conf.urls import patterns, include, url
from clustering.clustering import doInitialClustering

from common.models import Document

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'', include('querying.urls')),
    url(r'^mine/', include('mining.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

doInitialClustering(Document.objects.all())