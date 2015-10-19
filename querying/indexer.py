from common.models import Document, Token 
from itertools import chain 
from collections import Counter
 
from querying.caching import retrieveFromCache 
from querying.caching import saveToCache 
from common.tokenizer import getTokensFromText

import re
import math 
import logging 
logger = logging.getLogger("eventbook") 
 
 
def retrieveFromIndex(query): 
    cache = retrieveFromCache(query) 
   
    if False: #(cache is not None) and (len(cache) > 0): 
        logger.debug('Cache contained results for this query!') 
        return cache 
    else: 
        logger.debug('No results in cache') 
        
        docNumber = len(Document.objects.all())  
        print(docNumber)
        
        Dicttfidf={}  #save tfidf
        Dicttf={}   #save tf
        
        for document in Document.objects.all():
            Dicttf[document] = 0.0
            Dicttfidf[document] = 0.0
                 
        words = query.split()#getTokensFromText(query)
        
        for word in words: 
            tokens = Token.objects.filter(name__iexact=word) 
            #tokens = Token.objects.filter(name__contains=word) 
            
            for token in tokens:                 
                titleResults = token.title_tokens.all()
                for document in titleResults:
                    Dicttf[document]+=1                            
                dateResults = token.date_tokens.all() 
                for document in dateResults:
                    Dicttf[document]+=1 
                locationResults = token.location_tokens.all() 
                for document in locationResults:
                    Dicttf[document]+=1 
                genreResults = token.genres_tokens.all() 
                for document in genreResults:
                    Dicttf[document]+=1 
                artistResults = token.artist_tokens.all() 
                for document in artistResults:
                    Dicttf[document]+=1 
                tagResults = token.tag_tokens.all() 
                for document in tagResults:
                    Dicttf[document]+=1 
                 
                chainedResults = chain(titleResults, dateResults, locationResults, genreResults, artistResults, tagResults) 
 
                documents=[]
                for document in chainedResults: 
                    if document not in documents: 
                        documents.append(document) 
                        #print(Dicttf[document])

                df = len(documents)
                idf = math.log((docNumber / df), 2)
                
                for document in documents:
                    Dicttfidf[document] += idf * Dicttf[document]
                    Dicttf[document] = 0.0

        #for map in Dicttfidf.items():
        #   print(map[1])
            
        ranklist = sorted(Dicttfidf.items(), key = lambda map : map[1], reverse=True)
        
        saveToCache(query, ranklist)
        
        return ranklist
