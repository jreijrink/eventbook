from django.core.cache import cache
from common.models import Document
import hashlib

import logging
logger = logging.getLogger("eventbook")

def retrieveFromCache(query):
    something = hashlib.sha256(query.encode('utf-8'))
    key = something.hexdigest().encode('utf-8')
    #logger.debug('Query key for \'' + str(query) + '\': ' + key)
    result = cache.get(key)
    
    if result is not None:
        logger.debug('Found ' + str(len(result)) + ' results in cache')
    else:
        logger.debug('Query not found in cache')
    
    return result

def saveToCache(query, documents):
    logger.debug('Save query: \'' + query + '\' in cache with ' + str(len(documents)) + ' documents')    
    key = hashlib.sha256(query.encode('utf-8')).hexdigest().encode('utf-8')
    cache.set(key, documents, None)