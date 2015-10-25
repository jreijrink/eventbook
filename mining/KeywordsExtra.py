from querying.rake import Rake
from nltk.stem.wordnet import WordNetLemmatizer
import re
import operator

def KeywordsExtra(text):
    tags=[]
    lentext=len(text)
    ## lemmatize the words in the text
    lem=WordNetLemmatizer()
    words=text.split()
    text=' '.join([lem.lemmatize(i) for i in words])
    
    ## extract keywords, output with scores  
    if lentext<10: ## when the description is too short we don't need keywords
        tags=None
    else:
        if lentext<50:
            rake1=Rake("C:/wamp/www/eventbook/mining/SmartStoplist.txt",3,3,1)
            tags=rake1.run(text)
        else:
            rake2=Rake("C:/wamp/www/eventbook/mining/SmartStoplist.txt",3,3,2)
            tags=rake2.run(text)
    return(tags)
  
             
            
    