from common.models import Document, Token 
from mining.decomposition import decomposeDocument
from common.tokenizer import getTokensFromText
#from querying.caching import retrieveFromCache 
#from querying.caching import saveToCache 
import re
import numpy
import math 
import logging 
from email._header_value_parser import TokenList
logger = logging.getLogger("eventbook") 


def vcspace(docTexts):    #original text
    
    tokenlist=[]
    for text in docTexts:
        text=decomposeDocument(text)  #every text becomes a list       
        text=getTokensFromText(text)
        for token in text:
            if token not in tokenlist:
                tokenlist.append(token)
    
    dict={}
    textNum=len(docTexts) # number of rows
    tokenNum=len(tokenlist) # number of columns 
    i=0
    for i in range(0,len(tokenlist)-1):
        for text in docTexts:
            dict[text]=[]
            cnt=Counter()
            for word in text:
                cnt[word] += 1
            #print(cnt[tokenlist[i]])
            dict[text][i]= cnt(tokenlist[i])   #dict[text][i] is the matrix
                

    k=0
    m=0
    normText1=0
    normText2=0
    for key1 in dict.keys():
        for key2 in dict.keys():
            for k in range(0,tokenNum-1):
                normText1=normText1+dict[key1][k]
                normText2=normText2+dict[key2][k]
                normText1=sqrt(normText1)
                normText2=sqrt(normText2)
            for k in range(0,tokenNum-1):
                Similarity[m]=result+dict[text1][k]*dict[text2][k]
            Similarity[m]=Similarity[m]/normText1/normText2
            m+=1
    
    return Similarity
    
        
                
        
    