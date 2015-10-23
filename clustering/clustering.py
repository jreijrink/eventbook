from __future__ import print_function
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import sys

km = None

def doInitialClustering(documents):
    tfidfMatrix = buildTDIDF(documents)
    initialClustering(tfidfMatrix)

def buildTDIDF(documents):
    docs = documentIterator(documents)
    tfidf_vectorizer = TfidfVectorizer(max_df=1.0, max_features=200000,
                                     min_df=0.0, stop_words='english',
                                     use_idf=True, ngram_range=(1,3))

    tfidf_matrix = tfidf_vectorizer.fit_transform(docs) #fit the vectorizer to synopses

    #print(tfidf_matrix.shape)

    #terms = tfidf_vectorizer.get_feature_names()

    #from sklearn.metrics.pairwise import cosine_similarity
    #dist = 1 - cosine_similarity(tfidf_matrix)
    return tfidf_matrix

def initialClustering(tfidf_matrix):
    global km
    num_clusters = 10

    km = KMeans(n_clusters=num_clusters)

    km.fit(tfidf_matrix)

    #clusters = km.labels_.tolist()

#Use this
def clusterDocument(document):
    global km
    prediction = km.predict(document)
    return prediction

class documentIterator:
    def __init__(self, documents):
        self.documents = documents
        self.i = 0
        self.n = len(documents)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            if self.documents[i].description == None:
                return self.__next__()
            return self.documents[i].description

        else:
            raise StopIteration()
