from common.models import Document, Token
from itertools import chain

from querying.caching import retrieveFromCache
from querying.caching import saveToCache

import logging
logger = logging.getLogger("eventbook")

def retrieveFromIndex(query):
    cache = retrieveFromCache(query)
  
    if cache is not None:
        logger.debug('Cache contained results for this query!')
        return cache
    else:
        logger.debug('No results in cache')
        
        documents = set()
        restultDocument = Document.objects.none()
        
        words = query.split()
        
        for word in words:
            tokens = Token.objects.filter(name__iexact=word)
            #tokens = Token.objects.filter(name__contains=word)
            for token in tokens:
                titleResults = token.title_tokens.all()
                dateRestuls = token.date_tokens.all()
                locationRestuls = token.location_tokens.all()
                genreRestuls = token.genres_tokens.all()
                artisRestuls = token.artist_tokens.all()
                tagRestuls = token.tag_tokens.all()
                
                restultDocument = chain(restultDocument, titleResults, dateRestuls, locationRestuls, genreRestuls, artisRestuls, tagRestuls)

        for document in restultDocument:
            if document not in documents:
                documents.add(document)

        # TF.IDF here
        
        saveToCache(query, documents);
        return documents
    