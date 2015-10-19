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
    subText = text;
    words = subText.split();
    for word in words:
        if not lemmalist(word):
            subText = subText;
        else: subText = ' '.join([i for i in lemmalist(word)]);
        print(subText);
        text = text + ' ' + subText;
    print(text);
    print("SYNONYMS ADDED");
    return text