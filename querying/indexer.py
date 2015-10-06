from common.models import Document, Tag
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
            #tags = Tag.objects.filter(name__iexact=word)
            tags = Tag.objects.filter(name__contains=word)
            for tag in tags:
                titleResults = tag.title_tag.all()
                dateRestuls = tag.date_tags.all()
                locationRestuls = tag.location_tag.all()
                genreRestuls = tag.genres_tags.all()
                artisRestuls = tag.artist_tags.all()
                tagRestuls = tag.tag_tags.all()
                
                restultDocument = chain(restultDocument, titleResults, dateRestuls, locationRestuls, genreRestuls, artisRestuls, tagRestuls)

        for document in restultDocument:
            if document not in documents:
                documents.add(document)

        # TF.IDF here
        
        saveToCache(query, documents);
        return documents
    