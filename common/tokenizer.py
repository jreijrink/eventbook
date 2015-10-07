from nltk.stem.snowball import SnowballStemmer
import nltk
import re

def getTokensFromText(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens


#def getTokensFromText(text):
 #   tokens = list()
  #  text_items = text.split(" ")
   # for text_item in text_items:
    #    tokens.append(text_item)
    #return tokens

def getTokensFromList(textList):
    tokens = list()
    for text in textList:
        tokens.append(text)
    return tokens
