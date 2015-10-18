from django.shortcuts import get_object_or_404, render

from querying.spellchecker import checkSpelling
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

    resultsFromIndexRetrieval = retrieveFromIndex(query)
    
    documents = resultsFromIndexRetrieval[0] #list
    rankings = resultsFromIndexRetrieval[1]  #this is the dictionary for"document<=>idf"
    
    ranklist=sorted(rankings.items(),key=lambda d:d[1],reverse=True)
    print(ranklist)
    print(documents)
    i=0
    for i in range(0,len(documents)-1):
        documents[i]=ranklist[i][0]

    
    processtime = time.time() - start
    context = {'documents': documents,'query': query, 'processtime': round(processtime, 4)}
    return render(request, 'querying/search.html', context)

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'querying/detail.html', {'document': document})
