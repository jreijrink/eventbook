from nltk.corpus import wordnet
import sys

# Returns a list with all synonyms for one word.
def lemmalist(str):
    syn_set = []
    for synset in wordnet.synsets(str):
        for item in synset.lemma_names():
            syn_set.append(item)
    return syn_set

# Returns a string containing all synonyms for the words in an input string.
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