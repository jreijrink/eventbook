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
    print(str(len(documents)) + " documents used to learn cluster! \n")
    
    global tfidf_vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_df=1.0, max_features=200000,
                                     min_df=0.0, stop_words='english',
                                     use_idf=True, ngram_range=(1,3))

    tfidf_matrix = tfidf_vectorizer.fit_transform(docs) #fit the vectorizer to synopses

    print(str(tfidf_matrix.shape) + " (documents, features) in the TFIDF matrix \n")

    #terms = len(tfidf_vectorizer.get_feature_names())
    
    #print(str(terms) + "\n")
    
    #from sklearn.metrics.pairwise import cosine_similarity
    #dist = 1 - cosine_similarity(tfidf_matrix)
    return tfidf_matrix

def initialClustering(tfidf_matrix):
    global km
    num_clusters = 10

    km = KMeans(n_clusters=num_clusters)

    km.fit(tfidf_matrix)

    clusters = km.cluster_centers_.tolist()
    
    number = 1
    for cluster in clusters:
        count = 0
        for featureAxis in cluster:
            if featureAxis > 0:
                count += 1
        print("Cluster " + str(number) + ": " + str(count) + " feature axis \n")
        number += 1

#Use this
def clusterDocument(document):
    global km
    if document.description != None:
        documents = list()
        documents.append(document)
        docVector = tfidf_vectorizer.transform(documentIterator(documents))
        prediction = km.predict(docVector)
        print("Document belongs to cluser: " + str(prediction))
    return document

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
