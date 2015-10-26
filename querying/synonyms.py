from nltk.corpus import wordnet
import sys

# Returns a list with all synonyms for one word.
def lemmalist(str):
    syn_set = []
    for synset in wordnet.synsets(str):
        text = synset.name()
        head, sep, tail = text.partition('.')
        syn_set.append(head)
    return syn_set

# Returns a string containing all synonyms for the words in an input string.
def returnSynonyms(text):
    subText = text;
    words = subText.split();
    for word in words:
        if not lemmalist(word):
            subText = subText;
        else: subText = ' '.join([i for i in lemmalist(word)]);
        text = text + ' ' + subText;
    return text