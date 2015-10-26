from django.shortcuts import get_object_or_404, render

from mining.scraper import findDocuments

from clustering.clustering import doInitialClustering

from common.models import Document
from common.models import Document

def index(request):
    if (len(Document.objects.all())):
        doInitialClustering(Document.objects.all())
    
    findDocuments()
    return render(request, 'mining/index.html')