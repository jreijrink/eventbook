from nltk.corpus import wordnet
import sys

def lemmalist(str):
    syn_set = []
    for synset in wordnet.synsets(str):
        for item in synset.lemma_names():
            syn_set.append(item)
    return syn_set

def returnSynonyms(text):
    print("ADDING SYNONYMS");
    words = text.split();
    for word in words:
        text = ' '.join([i for i in lemmalist(word)]);
    print(text);
    print("SYNONYMS ADDED");
    return text