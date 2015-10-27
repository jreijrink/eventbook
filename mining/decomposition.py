from mining.contractions import expandContractions
from collections import OrderedDict
from nltk.stem.wordnet import WordNetLemmatizer
import re, string

def decompose(text, keepOriginal):
    if text:
        # Case-folding
        text = text.lower();
        
        # Expand all contractions like "isn't" to "is not"
        text = expandContractions(text);
        
        # Remove punctuation
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        text = regex.sub('', text)
        
        # Remove stop words (just add words to the list you think also have to be removed)
        stopWords = ['the','this','that','those','these','to','as','there','has','and','or',
                     'is','not','a','an','of','but','in','by','on','are','it','if'];
        words = text.split();
        text = ' '.join([i for i in words if i not in stopWords]);
        
        # Lemmatization
        lemmatizer = WordNetLemmatizer();
        words = text.split();
        if keepOriginal:
            text = ' '.join([i + " " + lemmatizer.lemmatize(i) for i in words]);
        else:            
            text = ' '.join([lemmatizer.lemmatize(i) for i in words]);
        
        # Remove duplicate words
        text = ' '.join(OrderedDict((word,word) for word in text.split()).keys());
    return text