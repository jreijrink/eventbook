from mining.contractions import expandContractions
from collections import OrderedDict
import re, string

def decomposeDocument(text):
    print("DECOMPOSITION");
    print(text);

    # Replace all uppercase letters to lowercase letters
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
    
    # Remove redundant words (just add words to the list you think also have to be removed)
    redundantWords = ['the','this','that','those','these','to','as','there','has','and','or','is','not','a','an','of','but','in','by','on','are','it','if'];
    words = text.split();
    text = ' '.join([i for i in words if i not in redundantWords]);
    print(text);
    
    print("END DECOMPOSITION");
    return text