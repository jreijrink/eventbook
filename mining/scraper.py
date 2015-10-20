from common.models import NewDocument

from mining.decomposition import decompose
from mining.classifier import multiLabelClassification
from mining.clustering import clusterDocument
from mining.duplication import findDuplicate

def findDocuments():

    # Example of how to create document
    document1 = NewDocument()

    document1.title = "Muse in Brussels"
    document1.description = "Everyone under 14 must be accompanied by an adult."
    document1.date = "March 12, 2016"
    document1.location = "L'Esplanade Brussels, Belgium 1030"
    
    document1.artists.append("Muse")
    
    document1.genres.append("Concerts")
    document1.genres.append("Tour Dates")
    
    document1.urls.append("http://brussels.eventful.com/events/muse-/E0-001-087441501-3")
    document1.imageUrls.append("http://s3.evcdn.com/images/block250/I0-001/000/273/446-5.jpg_/muse-46.jpg")
    
    document1.description = decompose(document1.description);
    document1 = multiLabelClassification(document1);
    document1 = clusterDocument(document1);
    document1 = findDuplicate(document1);
    
    document1.save()
    
    document2 = NewDocument()

    document2.title = "Comedy Night in Koningshooikt"
    document2.description = "Vier comedians treden op 24/10 aan voor een gezellige avond vol Comedy, 3 opkomende talenten en 1 headliner zorgen voor een gevarieerd aanbod. Jeron Dewulf kennen we van 'Foute Vrienden' op tv, op het podium met 3 talenten uit de stal van Independent Comedy Peter Gysen, Tom Cools en Dennis Vansant . VVK via Jong Jut en krantenwinkel Het Nieuwspunt te Koningshooikt."
    document2.date = "October 24, 2015 Saturday   8:30 PM"
    document2.location = "Mechelbaan 22 Koningshooikt, Antwerpen"
    
    document2.genres.append("Nightlife")
    document2.genres.append("Singles")
    document2.genres.append("Comedy")
    
    document2.urls.append("http://eventful.com/events/comedy-night-/E0-001-087361484-8")
    document2.imageUrls.append("http://s3.evcdn.com/images/block250/I0-001/022/049/054-1.jpeg_/comedy-night-54.jpeg")
    
    document2.description = decompose(document2.description);
    document2 = multiLabelClassification(document2);
    document2 = clusterDocument(document2);
    document2 = findDuplicate(document2);
    
    document2.save()
    
    document3 = NewDocument()

    document3.title = "Theater op de Markt in Neerpelt"
    document3.description = "Van 30 oktober tot 3 november verandert het domein van Dommelhof in een gezellig circusdorp. Circusartiesten uit België en ver daarbuiten slaan er hun tenten op voor de negende editie van het internationaal circustheaterfestival van Theater op de Markt. Theater op de Markt biedt voorstellingen voor volwassenen en kinderen, echte familiecircussen in authentieke circustenten, intieme theatervoorstellingen met circus als rode draad en circustheater op speciale buitenlocaties. Theater op de Markt wil als festival voor iedereen toegankelijk zijn en biedt een programma aan waarin iedereen zijn gading kan vinden. Het programma bestaat uit een mix van gratis voorstellingen en voorstellingen aan democratische ticketprijzen.  Meer info: www.theateropdemarkt.be of www.dommelhof.be"
    document3.date = "October 30, 2015"
    document3.location = "Toekomstlaan 5 Neerpelt, Limburg"
    
    document3.genres.append("Festivals")
    
    document3.urls.append("http://eventful.com/events/theater-op-markt-/E0-001-078303346-1")
    document3.imageUrls.append("http://s1.evcdn.com/images/block250/I0-001/021/462/140-5.jpeg_/theater-op-markt-40.jpeg")
    
    document3.description = decompose(document3.description);
    document3 = multiLabelClassification(document3);
    document3 = clusterDocument(document3);
    document3 = findDuplicate(document3);
    
    document3.save()
    
    document4 = NewDocument()

    document4.title = "Florence And The Machine in Antwerp"
    document4.description = "FLORENCE AND THE MACHINE"
    document4.date = "December 9, 2015 Wednesday   7:00 PM"
    document4.location = "Schijnpoortweg 113 Antwerp, Antwerpen"
    
    document4.artists.append("Florence And The Machine")
    document4.genres.append("Concerts")
    document4.genres.append("Tour Dates")
    
    document4.urls.append("http://eventful.com/antwerp/events/florence-and-machine-/E0-001-085017860-2")
    document4.imageUrls.append("http://s4.evcdn.com/images/block250/I0-001/002/397/451-8.jpeg_/florence-and-the-machine-51.jpeg")
    
    document4.description = decompose(document4.description);
    document4 = multiLabelClassification(document4);
    document4 = clusterDocument(document4);
    document4 = findDuplicate(document4);
    
    document4.save()
