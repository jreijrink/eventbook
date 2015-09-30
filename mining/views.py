from django.shortcuts import get_object_or_404, render

from mining.scraper import findDocuments

from common.models import Document

def index(request):
    findDocuments()
    return render(request, 'mining/index.html')