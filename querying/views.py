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
    #documents = createSuggestions()
    #context = {'suggestions': documents}
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
    
    suggestions = createSuggestions(original, results[0])
    
    pages = ceil(results[1] / eventbook_settings.PAGE_SIZE)   
    processtime = time.time() - start
    
    pagestart = max(1, page - 5)
    pageend = min(pages, page + 5)
        
    context = {'documents': results[0], 'query': original, 'extendedquery': query, 'results': results[1], 'page': page, 'totalpages': pages, 'pages': range(pagestart, pageend + 1), 'prev': max(1, page - 1), 'next': min(pages, page + 1), 'processtime': round(processtime, 4), 'suggestions': suggestions}
    
    return render(request, 'querying/search.html', context)

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'querying/detail.html', {'document': document})
