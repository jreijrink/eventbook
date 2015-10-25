
from common.models import Document, Token 
from itertools import chain 
from collections import Counter
from mining.decomposition import decompose
from common.tokenizer import getTokensFromText
from mining.contractions import expandContractions
from collections import OrderedDict
from nltk.stem.wordnet import WordNetLemmatizer
import re, string
import operator
### query expansion based on pseudo relevance feedback(we use top 5 results as relevant documents )
### input the original query and relevant documents
def createSuggestions(query,documents): ## input the original query and relevant documents(Top 5 documents retrieved in our case)
    doclists=[]
    rowlists=[]
    #n=0
    tokenlist=[]
    for text in documents:
        text=decompose(text)  #every text becomes a list
        list=getTokensFromText(text)       
        doclists.append(list)
        for token in list:
            if token not in tokenlist:
                tokenlist.append(token)
        list=[]
        rowlists.append(list)
    ## deal with query
    query=decompose(query)
    print(query)
    list=getTokensFromText(query)
    doclists.insert(0,list)
    #query=list
    list=[]
    rowlists.insert(0,list)
    
    for list in rowlists:  #initialize
        i=0
        for i in range(0,len(tokenlist)): 
            list.append(0)
    i=0
    print(tokenlist)
    n=-1
    for list in doclists:
        n=n+1
        for i in range(0,len(list)):
            if list[i] in tokenlist:
                index=tokenlist.index(list[i])
                rowlists[n][index]=rowlists[n][index]+1     

    score={}
    for i in range(0,len(tokenlist)-1):
        score[tokenlist[i]]=rowlists[0][i]
        for j in range(1,len(rowlists)-1):
            score[tokenlist[i]]=score[tokenlist[i]]+0.75*rowlists[j][i]
    rankwords = sorted(score.items(), key = lambda map : map[1], reverse=True)
    print(rankwords)
    
    ## load stopwords
    stopwords=open("C:/wamp/www/eventbook/querying/sSmartStoplist.txt")
    stop_words = []
    for line in stopwords:
        if line.strip()[0:1] != "#":
            for word in line.split():  # in case more than one per line
                stop_words.append(word) 
    print(stop_words) 
    ## generate new query
    ## find words with score bigger than 1.5 and don't show in the original query and the stop_words.
    print(rankwords[0][1])
    print(rankwords[0][0])
    newrank=[]
    print(len(query))
    for i in range(0,len(tokenlist)-1):
        if rankwords[i][1]>=1.5 and rankwords[i][0] not in query and rankwords[i][0] not in stop_words:
            newrank.append(rankwords[i][0])    
    k=len(newrank)
     ## if there are no words in newrank, we don't have expanded query
    if k==0:
        quer=None
    else:
        quer=[[],[],[]]
        if k>3:      ###  we only generate at most 3 new queries
            k=3   
        for i in range(0,k):
            quer[i].append(query)
            quer[i].append(newrank[i])
            quer[i]=' '.join(i for i in quer[i])
    print(quer)
    return quer