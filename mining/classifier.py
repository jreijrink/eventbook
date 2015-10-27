from querying.rake import Rake
from nltk.stem.wordnet import WordNetLemmatizer
import re
import operator
from eventbook import settings as eventbook_settings
from common.tokenizer import getTokensFromText

def multiLabelClassification(document):
    #print("Start classification")
    if document.description:
        text = document.description
        
        lentext=len(text)
        
        ## lemmatize the words in the text
        lem = WordNetLemmatizer()
        words=text.split()
        text=' '.join([lem.lemmatize(i) for i in words])
        
        ## extract keywords, output with scores  
        if lentext<10: ## when the description is too short we don't need keywords
            tags=None
        else:
            if lentext<150:
                rake = Rake(eventbook_settings.PROJECT_ROOT + "common/SmartStoplist.txt",3,3,1)
                tags = rake.run(text)
            else:
                rake = Rake(eventbook_settings.PROJECT_ROOT + "common/SmartStoplist.txt",3,3,2)
                tags = rake.run(text)
                
        if tags:
            for tag in tags:
                tokens = getTokensFromText(tag[0])
                for token in tokens:
                    document.tags.append(token)
                    #print("Found token: " + token)

    #print("End classification")
    return document