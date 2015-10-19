from common.models import Document, Token 
from common.tokenizer import getTokensFromText
from common.tokenizer import getTokensFromList
from eventbook import settings as eventbook_settings

def findDuplicate(document):
    
    print("START DUP");
    
    results = []
 
    # Check for the same title tokens, must be exactly the same   
    titleTokens = getTokensFromText(document.title)
    
    for index, titleToken in enumerate(titleTokens):
        tokens = Token.objects.filter(name=titleToken)
        
        for token in tokens:         
            documentResults = token.title_tokens.all()
            
            if index == 0:
                for result in documentResults: 
                    if result not in results: 
                        results.append(result)
            else:
                results = list(set(results) & set(documentResults))
    
    if len(results) > 0:
        document.duplication = findDuplicateInResults(document, results)
    
    print("END DUP");
    return document

def findDuplicateInResults(document, results):
    for result in results:
        for url in result.urls.all():
            # If the same url -> definitly duplicate
            if url.name in document.urls:
                print("FOUND DUPLICATE");
                return result

        # Check for overlap in Artist, Genre, Location and Date
        if (hasOverlap(getTokensFromText(document.date), result.date.all()) and 
            hasOverlap(getTokensFromText(document.location), result.location.all()) and 
            hasOverlap(getTokensFromList(document.genres), result.genres.all()) and 
            hasOverlap(getTokensFromList(document.artists), result.artists.all())):
            
            print("FOUND DUPLICATE");
            return result
    
def hasOverlap(textSet, tokenSet):
    if len(textSet) > 0 and len(tokenSet) > 0:
        tokenNameSet = set()
        for token in tokenSet:
            tokenNameSet.add(token.name)
        
        uniqueCount = len(set(list(textSet) + list(tokenNameSet)))
        overlapCount = len(list(set(textSet) & set(tokenNameSet)))
        
        overlapPercentage = overlapCount / uniqueCount;
        
        print("PERCENTAGE: " + str(overlapPercentage))
        
        # Certain amount of overlap is required! Value can be configured in the seetings
        if overlapPercentage >= eventbook_settings.DUPLICATION_LIMIT:
            return True
        else:
            return False
            
    #If any set it empty then accept the overlap
    return True
