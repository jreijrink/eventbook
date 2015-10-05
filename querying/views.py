from django.shortcuts import get_object_or_404, render

from querying.spelchecker import checkSpelling
from querying.decomposition import decompose
from querying.searchhistory import applySearchHistory
from querying.indexer import retrieveFromIndex
from querying.suggestor import createSuggestions

from common.models import Document
import time

def index(request):
    documents = createSuggestions()
    context = {'suggestions': documents}
    return render(request, 'querying/index.html')

def search(request):
    start = time.time()
    query = request.GET.get('q', '')
    
    query = checkSpelling(query)
    query = decompose(query)
    query = applySearchHistory(query)
    
    documents = retrieveFromIndex(query)
    
    processtime = time.time() - start
    context = {'documents': documents, 'query': query, 'processtime': round(processtime, 4)}
    return render(request, 'querying/search.html', context)

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'querying/detail.html', {'document': document})
