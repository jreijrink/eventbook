from nltk.stem.snowball import SnowballStemmer
import nltk
import re

def getTokensFromText(text):
    tokens = list()
    
    if text is not None and text is not '':
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        for sentence in nltk.sent_tokenize(text):
             for word in nltk.word_tokenize(sentence):
                token = word.lower()
                # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
                #if re.search('[a-zA-Z]', token):
                tokens.append(token)

    return tokens

def getTokensFromList(textList):
    tokens = list()
    for text in textList:   
        tokens.extend(getTokensFromText(text))
    return tokens
