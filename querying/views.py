from django.shortcuts import get_object_or_404, render

from querying.spellchecker import checkSpelling
from mining.decomposition import decompose
from querying.synonyms import returnSynonyms
from querying.searchhistory import applySearchHistory
from querying.indexer import retrieveFromIndex
from querying.suggestor import createSuggestions
from eventbook import settings as eventbook_settings
from math import ceil

from common.models import Document
import time
from django.core.paginator import Page

def index(request):
    documents = createSuggestions()
    context = {'suggestions': documents}
    return render(request, 'querying/index.html')

def search(request):
    start = time.time()
    query = request.GET.get('q', '')
    original = query
    page = request.GET.get('p', '')
    if not page:
        page = 1
    else:
        page = int(page)
    
    query = checkSpelling(query)
    query = decompose(query)
    query = returnSynonyms(query)
    query = decompose(query)
    query = applySearchHistory(query)

    results = retrieveFromIndex(query, page)
    
    pages = ceil(results[1] / eventbook_settings.PAGE_SIZE)   
    processtime = time.time() - start
    
    context = {'documents': results[0], 'query': original, 'extendedquery': query, 'page': page, 'pages': range(1, pages + 1), 'prev': max(1, page - 1), 'next': min(pages, page + 1), 'processtime': round(processtime, 4)}
    
    return render(request, 'querying/search.html', context)

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'querying/detail.html', {'document': document})
