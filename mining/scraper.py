import urllib.request

from bs4 import BeautifulSoup

from common.models import NewDocument
from mining.decomposition import decompose
from mining.classifier import multiLabelClassification
from clustering.clustering import clusterDocument
from mining.duplication import findDuplicate

def findDocuments():
    
    urlEventfull = '.eventful.com/events?q=*&ga_search=*&ga_type=events&sort_order=Popularity&page_number='
    urlSongKick = 'http://www.songkick.com/session/filter_metro_area'
    
    request = urllib.request.Request(urlSongKick)
    response = urllib.request.urlopen(request, timeout=5)
    
    soup = BeautifulSoup(response.read(),"html5lib")
    eventLinks = soup.find(attrs={"class": "component popular-metro-areas"})
    
    eventfulLinks = set()
    songkickLinks = set()
    
    locationSize = len(eventLinks.find_all('a'))
    
    for index, link in enumerate(eventLinks.find_all('a')):
        
        #TEMP FOR TESTING
        if index > 0:
            break
        
        location= link.string.split(',')[0].replace(' ','').lower()
        
        if (location=='sfbayarea'):
            location='sanfrancisco'
        else:
            if (location=='newyork'):
                location='newyorkcity'
        
        urlSongKick='http://www.songkick.com'+link['href']
        
        #print("searching eventful links for " + location + " " + str(index) + "/" + str(locationSize))
        eventfulLinks.update(getEventfulLinks(location, urlEventfull))
        
        #print("searching songkick links for " + location + " " + str(index) + "/" + str(locationSize))
        songkickLinks.update(getSongkickLinks(location, urlSongKick))
        
        totalLink = len(eventfulLinks) + len(songkickLinks)
        #print("found " + str(totalLink) + " links so far. (" + str(len(eventfulLinks)) + " EVENTFUL, " + str(len(songkickLinks)) + " SONGKICK)")
    
    totalLink = len(eventfulLinks) + len(songkickLinks)
    #print("Found all " + str(totalLink) + " link, now start processing them")
    
    for index, eventLink in enumerate(eventfulLinks):
        doc = getEventfulDocument(eventLink)
        processAndSaveDoc(doc)
        #print("Processed " + str(index) + " / " + str(len(eventfulLinks)) + " links for eventful (" + str(index) + " / " + str(totalLink) + " total)")
        
    for index, eventLink in enumerate(songkickLinks):
        doc = getSongkickDocument(eventLink)
        processAndSaveDoc(doc)
        #print("Processed " + str(index) + " / " + str(len(songkickLinks)) + " links for eventful (" + str(index + len(eventfulLinks)) + " / " + str(totalLink) + " total)")

def getEventfulLinks(location, url): 
    
    links = set()
    
    try:
        request = urllib.request.Request('http://'+location + url)
        response = urllib.request.urlopen(request, timeout=30)
    
        soup = BeautifulSoup(response.read(),"html5lib")     
        results = soup.find(attrs={"class": "results-count"}).string.split()[0]
        
        endpage= int((int(results.split(',')[0])*1000+int(results.split(',')[1]))/15)
        beginpage = 1    
        
        #TEMP FOR TESTING
        endpage = min(1, endpage)
        
        for i in range(beginpage, endpage + 1):
            try:
                #print("Processing page " + str(i) + "/" + str(endpage))
                    
                pageRequest = urllib.request.Request('http://' + location + url + str(i))
                pageResponse = urllib.request.urlopen(pageRequest, timeout=5)
                pages = BeautifulSoup(pageResponse.read(), "html5lib")
        
                for page in pages.find_all('a'):
                    if 'data-ga-label' in page.attrs and page['data-ga-label'] == 'Event Title Link':
                        links.add(page['href'])
            except:
                print("An ERROR occured for this page!")
    except:
        print("An ERROR occured for this location!")
        
    return links

def getSongkickLinks(location, url):
    
    links = set()
    
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request, timeout=5)
    
        soup = BeautifulSoup(response.read(), "html5lib")
        
        endpage = int(soup.find(attrs={"class":"next_page"}).previous_sibling.previous_sibling.string)
        beginpage = 1
        
        #TEMP FOR TESTING
        endpage = min(0, endpage)
        
        for i in range(beginpage, endpage + 1):  
            try:
                print("Processing page " + str(i) + "/" + str(endpage))
                
                pageRequest = urllib.request.Request(url + '?page=' + str(i))
                pageResponse = urllib.request.urlopen(pageRequest, timeout=5)
                pages = BeautifulSoup(pageResponse.read(), "html5lib")
                
                for page in pages.find_all(attrs={"class":'artists summary'}):
                    link = 'http://www.songkick.com' + page.a['href']
                    links.add(link)
            except:
                print("An ERROR occured for this page!")
            
    except:
        print("An ERROR occured for this location!")
        
    return links
    
def getEventfulDocument(link):
    #try:
        eventRequest = urllib.request.Request(link)
        eventResponse = urllib.request.urlopen(eventRequest)
        eventSoup = BeautifulSoup(eventResponse.read(), "html5lib")
        
        document = NewDocument()
        
        title = ''
        titleContainer = eventSoup.h1.find_all('span')
        if titleContainer:
            for span in titleContainer:
                title += str(span.text)
        document.title = title
        
        eventdate=''
        dateContainer = eventSoup.find_all(attrs={"itemprop": "startDate"})
        if dateContainer:
            for event in dateContainer:
                eventdate += str(event.text)
        document.date = eventdate
        
        location = ''
        locationContainer = eventSoup.find_all(attrs={"itemprop": "location"})
        if locationContainer:
            for span in locationContainer:
                location += span.p.text
        document.location = location
                
        description = eventSoup.find(attrs={"class": "section-block description"})
        if description:
            document.description = description.p.string
        
        genreContainer = eventSoup.find(attrs={"class": "section-block description"})
        if genreContainer:
            last_p = None
            for last_p in genreContainer.findAll('p'):pass
            if last_p:
                document.genres.append(last_p.a.text)
            
        artistContainer = eventSoup.find(attrs={"itemprop": "performer"})
        if artistContainer:
            document.artists.append(artistContainer.span.string)
        
            artistLink = artistContainer.a['href']
            artistRequest = urllib.request.Request(artistLink)
            artistResponse = urllib.request.urlopen(artistRequest)
            artistSoup = BeautifulSoup(artistResponse.read(), "html5lib")
            
            document.genres.append(artistSoup.h5.string)
            
        image = eventSoup.find(attrs={"class": "image-viewer-open"})
        if image:
            document.imageUrls.append(image.img['src'])

        document.urls.append(link)
        return document
    
    #except:
    #    print("An ERROR occured for this document!")
    
def getSongkickDocument(link):
    try:
        eventRequest = urllib.request.Request(link)
        eventResonse = urllib.request.urlopen(eventRequest, timeout=5)
        eventSoup = BeautifulSoup(eventResonse.read(), "html5lib")
        
        document = NewDocument()
        
        title = ''
        titleContainer = eventSoup.h1.span.find_all('a')
        if titleContainer:
            for a in titleContainer:
                title += str(a.text)
        document.title = title
                
        details = ''
        detailsContainer = eventSoup.find(attrs={"class":'additional-details-container'})
        if detailsContainer:
            for p in detailsContainer:
                details += str(p.string)
        document.description = details
        
        document.date = eventSoup.h5.string
        
        location = ''
        locationContainer = eventSoup.find_all("div", { "class":'location'})
        if locationContainer:
            for span in locationContainer:
                location += str(span.text)
        document.location = location
        
        performer = ''
        artistContainer = eventSoup.find_all(attrs={"class":'line-up'})
        if artistContainer:
            for span in artistContainer:
                performer += str(span.a.text)                                    
        document.artists.append(performer)
    
        image = eventSoup.find(attrs={"class": "profile-picture-wrapper"})
        if image:
            document.imageUrls.append(image.img['src'])
        
        document.urls.append(link)
        return document
    except:
        print("An ERROR occured for this document!")
    
def processAndSaveDoc(document):   
    # try:
        if document:
            document.description = decompose(document.description, False);
            document = multiLabelClassification(document);
            document = clusterDocument(document);
            document = findDuplicate(document);
            
            document.save()
    # except:
    #     print("An ERROR occured in processing!")
