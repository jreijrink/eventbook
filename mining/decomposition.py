from mining.contractions import expandContractions
from collections import OrderedDict
from nltk.stem.wordnet import WordNetLemmatizer
import re, string

def decomposeDocument(text):
    print("DECOMPOSITION");
    print(text);

    # Case-folding
    text = text.lower();
    print(text);
    
    # Expand all contractions like "isn't" to "is not"
    text = expandContractions(text);
    print(text);
    
    # Remove punctuation
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    text = regex.sub('', text)
    print(text);
    
    # Remove duplicate words
    text = ' '.join(OrderedDict((word,word) for word in text.split()).keys());
    print(text);
    
    # Remove stop words (just add words to the list you think also have to be removed)
    stopWords = ['the','this','that','those','these','to','as','there','has','and','or','is','not','a','an','of','but','in','by','on','are','it','if'];
    words = text.split();
    text = ' '.join([i for i in words if i not in stopWords]);
    print(text);
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer();
    words = text.split();
    text = ' '.join([lemmatizer.lemmatize(i) for i in words]);
    print(text);
    
    print("END DECOMPOSITION");
    return text