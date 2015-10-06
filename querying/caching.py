from django.core.cache import cache
from common.models import Document
import hashlib

import logging
logger = logging.getLogger("eventbook")

def retrieveFromCache(query):
    key = hashlib.sha256(query.encode('utf-8')).hexdigest()
    logger.debug('Query key for \'' + str(query) + '\': ' + key)
    result = cache.get(key)
    
    if result is not None:
        logger.debug('Found ' + str(len(result)) + ' results in cache')
    else:
        logger.debug('Query not found in cache')
    
    return result

def saveToCache(query, documents):
    logger.debug('Save query: \'' + query + '\' in cache with ' + str(len(documents)) + ' documents')    
    key = hashlib.sha256(query.encode('utf-8')).hexdigest()
    cache.set(key, documents, None)