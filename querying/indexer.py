from common.models import Document, Token 
from itertools import chain 
 
 
from querying.caching import retrieveFromCache 
from querying.caching import saveToCache 

 
import logging 
import math
logger = logging.getLogger("eventbook") 
 
 
def retrieveFromIndex(query): 
    cache = retrieveFromCache(query) 
    
    if cache is not None: 
        logger.debug('Cache contained results for this query!') 
        return cache 
    else: 
        logger.debug('No results in cache') 
         
        docnumber = len(Document.objects.all())
        print(docnumber)

        Dict={}
        for document in Document.objects.all():#something wrong
            Dict[document]=0.0
            print(Dict[document])
           
        words = query.split() 
         
        for word in words: 
            tokens = Token.objects.filter(name__iexact=word) 
            #tokens = Token.objects.filter(name__contains=word) 
            for token in tokens: 
                resultDocument=set()
                titleResults = token.title_tokens.all() 
                dateResults = token.date_tokens.all() 
                locationResults = token.location_tokens.all() 
                genreResults = token.genres_tokens.all() 
                artistResults = token.artist_tokens.all() 
                tagResults = token.tag_tokens.all()
                 
                resultDocument = chain(resultDocument, titleResults, dateResults, locationResults, genreResults, artistResults, tagResults) 

                documents = set()

                for document in resultDocument: 
                    if document not in documents: 
                        documents.add(document) 

                
                df = len(documents)
                print(df)
                idf=math.log((docnumber/df),2)
                print(idf)
                
                for document in documents:
                    Dict[document] +=  idf
        # TF.IDF here 
        # 

 

 
        saveToCache(query, documents); 
        return documents 
