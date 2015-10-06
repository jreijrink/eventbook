'''
Created on Oct 6, 2015

@author: Yuehan  
I found this code on wiki, but really don't know how it works and how to connect with database.
'''
from pprint import pprint as pp
from glob import glob
from functools import reduce
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input
 
 
def parsetexts(fileglob='InvertedIndex/T*.txt'):
    texts, words = {}, set()
    for txtfile in glob(fileglob):
        with open(txtfile, 'r') as f:
            txt = f.read().split()
            words |= set(txt)
            texts[txtfile.split('\\')[-1]] = txt
    return texts, words
 
def termsearch(terms): # Searches simple inverted index
    return reduce(set.intersection,
                  (invindex[term] for term in terms),
                  set(texts.keys()))
 
texts, words = parsetexts()
print('\nTexts')
pp(texts)
print('\nWords')
pp(sorted(words))
 
invindex = {word:set(txt
                        for txt, wrds in texts.items() if word in wrds)
            for word in words}
print('\nInverted Index')
pp({k:sorted(v) for k,v in invindex.items()})
 
terms = ["what", "is", "it"]
print('\nTerm Search for: ' + repr(terms))
pp(sorted(termsearch(terms)))


'''Outputs:
Texts
{'T0.txt': ['it', 'is', 'what', 'it', 'is'],
 'T1.txt': ['what', 'is', 'it'],
 'T2.txt': ['it', 'is', 'a', 'banana']}

Words
['a', 'banana', 'is', 'it', 'what']

Inverted Index
{'a': ['T2.txt'],
 'banana': ['T2.txt'],
 'is': ['T0.txt', 'T1.txt', 'T2.txt'],
 'it': ['T0.txt', 'T1.txt', 'T2.txt'],
 'what': ['T0.txt', 'T1.txt']}

Term Search for: ['what', 'is', 'it']
['T0.txt', 'T1.txt']'''