from sklearn.cluster import KMeans

def initialClustering(tfidf_matrix):
    num_clusters = 5 #chang

    km = KMeans(n_clusters=num_clusters)

    km.fit(tfidf_matrix)

    clusters = km.labels_.tolist()

    return km

def clusterDocument(km, document):

    return km.predict(document)

# def clusterDocument(document):
#    return document
