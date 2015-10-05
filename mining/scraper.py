from common.models import NewDocument

from mining.decomposition import decomposeDocument
from mining.classifier import multiLabelClassification
from mining.clustering import clusterDocument
from mining.duplication import findDuplicate

def findDocuments():

    # Example of how to create document
    document = NewDocument()

    document.title = "Festival Title"
    document.description = "This isn't a Festival title, but it's a Festival description...!"
    document.date = "01-01-2016"
    document.location = "New York"
    
    document.genres.append("Dance")
    document.genres.append("Pop")
    
    document.artists.append("Who")
    
    document.tags.append("tag1")
    document.tags.append("tag2")
    document.tags.append("tag3")
    
    document.urls.append("http://eventful.com/event/12")
    document.imageUrls.append("http://eventful.com/event/12/logo.jpg")
    
    document.description = decomposeDocument(document.description);
    document = multiLabelClassification(document);
    document = clusterDocument(document);
    document = findDuplicate(document);
    
    document.save()
