from common.models import Document, Token 
from itertools import chain 
from collections import Counter
 
from querying.caching import retrieveFromCache 
from querying.caching import saveToCache 
from common.tokenizer import getTokensFromText
from eventbook import settings as eventbook_settings

import re
import math 

#import logging 
#logger = logging.getLogger("eventbook") 
 
def retrieveFromIndex(query, page): 
    cache = retrieveFromCache(query) 
   
    if (cache is not None) and page == 1:
        #logger.debug('Cache contained results for this query!') 
        return cache 
    else: 
        #logger.debug('No results in cache') 
        
        docNumber = len(Document.objects.all())
        
        Dicttfidf={}  #save tfidf
        Dicttf={}   #save tf
                         
        words = query.split()#getTokensFromText(query)
        
        for word in words: 
            tokens = Token.objects.filter(name=word)
            #tokens = Token.objects.filter(name__iexact=word)
            #tokens = Token.objects.filter(name__contains=word) 
            
            for token in tokens:  
                    
                titleResults = token.title_tokens.all()
                for document in titleResults:
                    incement_set(Dicttf, document, 1)                            
                dateResults = token.date_tokens.all() 
                for document in dateResults:
                    incement_set(Dicttf, document, 1)
                locationResults = token.location_tokens.all() 
                for document in locationResults:
                    incement_set(Dicttf, document, 1)
                genreResults = token.genres_tokens.all() 
                for document in genreResults:
                    incement_set(Dicttf, document, 1)
                artistResults = token.artist_tokens.all() 
                for document in artistResults:
                    incement_set(Dicttf, document, 1)
                tagResults = token.tag_tokens.all() 
                for document in tagResults:
                    incement_set(Dicttf, document, 1)
                 
                documents = list(set(chain(titleResults, dateResults, locationResults, genreResults, artistResults, tagResults)))
 
                df = len(documents)
                idf = math.log((docNumber / df), 2)
                
                for document in documents:
                    incement_set(Dicttfidf, document, idf * Dicttf[document])
                    Dicttf[document] = 0.0

        ranklist = sorted(Dicttfidf.items(), key = lambda map : map[1], reverse=True)
        
        resultSize = len(ranklist)
        pageResults = ranklist[(page - 1) * eventbook_settings.PAGE_SIZE : page * eventbook_settings.PAGE_SIZE ]
        
        results = (pageResults, resultSize)
        if page == 1:
            saveToCache(query, results)
        
        return results

def incement_set(dict_set, key, incemental):
    if key in dict_set:
        dict_set[key] += incemental
    else:
        dict_set[key] = incemental
        