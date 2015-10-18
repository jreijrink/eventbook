from common.models import Document, Token 
from itertools import chain 
from collections import Counter
 
from querying.caching import retrieveFromCache 
from querying.caching import saveToCache 
 
import re
import math 
import logging 
logger = logging.getLogger("eventbook") 
 
 
def retrieveFromIndex(query): 
    cache = retrieveFromCache(query) 
   
    if (cache is not None) and (len(cache) > 0): 
        logger.debug('Cache contained results for this query!') 
        return cache 
    else: 
        logger.debug('No results in cache') 
        
        docNumber = len(Document.objects.all())  
        print(docNumber)
        Dicttfidf={}  #save tfidf
        for document in Document.objects.all():
            Dicttfidf[document]=0.0
            
        Dicttf={}   #save tf
        for document in Document.objects.all():
            Dicttf[document]=0.0
        
        
        #documents = set()
        documents=[]
        resultDocument = Document.objects.none() 
         
        words = query.split() 
         
        for word in words: 
            tokens = Token.objects.filter(name__iexact=word) 
            #tokens = Token.objects.filter(name__contains=word) 
            for token in tokens: 
                #resultDocument = set()
                resultDocument=[]
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
                 
                resultDocument = chain(resultDocument, titleResults, dateResults, locationResults, genreResults, artistResults, tagResults) 

 
                for document in resultDocument: 
                    if document not in documents: 
                        documents.append(document) 
                        #print(Dicttf[document])
                        
                df = len(documents)
                idf=math.log((docNumber/df),2)
                
                for document in documents:
                    Dicttfidf[document] +=  idf*Dicttf[document]
                
                for document in Document.objects.all():
                    Dicttf[document]=0.0
                    
                    

        for document in Document.objects.all():
            print(Dicttfidf[document])
 

        Tuple=(documents,Dicttfidf)
        saveToCache(query, documents)
        
        return Tuple
