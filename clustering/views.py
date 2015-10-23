from django.shortcuts import get_object_or_404, render
import clustering.clustering

from common.models import Document

def index(request):
    clustering.clustering.doInitialClustering(Document.objects.all())
    return render(request, 'clustering/index.html')