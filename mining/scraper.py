from common.models import NewDocument

from mining.decomposition import decomposeDocument
from mining.classifier import multiLabelClassification
from mining.clustering import clusterDocument
from mining.duplication import findDuplicate

import urllib.request
from bs4 import BeautifulSoup

def findDocuments(location,url,Sname):
#读入对应网站所有链接，并保存到对应txt文档内
 
    if (url.split('.')[1]=='eventful'):   
        request=urllib.request.Request('http://'+location+url)
        response = urllib.request.urlopen(request, timeout=30)
        #抓取页面内容
        soup = BeautifulSoup(response.read(),"html5lib")     
        s=soup.find(attrs={"class": "results-count"}).string.split()[0]
        endpage= int((int(s.split(',')[0])*1000+int(s.split(',')[1]))/15)
        Sname='eventful\\'+Sname
        ft=open(Sname,'w')
        beginpage = 1    
        for i in range(beginpage,endpage+1):
            request1=urllib.request.Request('http://'+location+url+str(i))
            response1 = urllib.request.urlopen(request1, timeout=5)
            soup1 = BeautifulSoup(response1.read(),"html5lib")
            #eventful 链接读入
            for a in soup1.find_all('a'):
                if 'data-ga-label' in a.attrs:
                    if a['data-ga-label'] == 'Event Title Link':
                        print (a['href'])
                        request2 = urllib.request.Request(a['href'])
                        response2 = urllib.request.urlopen(request2)
                        soup2 = BeautifulSoup(response2.read(),"html5lib")
                        document = NewDocument()
                        title = ''
                        for span in soup2.h1.find_all('span'):
                            title += span.text
                        document.title = title
                        eventdata=''
                        for event in soup2.find_all(attrs={"itemprop": "startDate"}):
                            eventdata += event.text
                        document.date = eventdata
                        document.location = soup2.h6.a.String
                        document.description = soup2.find(attrs={"class": "section-block description"}).p.string
                        document.artists.append=(soup2.find(attrs={"itemprop": "performer"}).span.string)
                        link=soup2.find(attrs={"itemprop": "performer"}).a['href']
                        request3 = urllib.request.Request(link)
                        response3 = urllib.request.urlopen(request3)
                        soup3 = BeautifulSoup(response3.read(),"html5lib")
                        document.genres.append(soup3.h5.string)
                        document.tags.append("tag1")
                        document.tags.append("tag2")
                        document.tags.append("tag3")
                        document.urls.append(a['href'])
                        document.imageUrls.append(soup3.find(attrs={"class": "image-viewer-open"}).img['src'])
                        document.description = decomposeDocument(document.description);
                        document = multiLabelClassification(document);
                        document = clusterDocument(document);
                        document = findDuplicate(document);
                        document.save()
                        ft.write(a['href']+'\n')
                        ft.close()
    else: 
        if (url.split('.')[1]=='songkick'):

                url1=url
                ft=open(Sname,'w')
                request1=urllib.request.Request(url1)
                response1 = urllib.request.urlopen(request1, timeout=5)
                #抓取页面内容
                soup1 = BeautifulSoup(response1.read(),"html5lib")
                endpage=int(soup1.find(attrs={"class":"next_page"}).previous_sibling.previous_sibling.string)
                beginpage=1
                for i in range(beginpage,endpage+1):
                    request2=urllib.request.Request(url1+'?page='+str(i))
                    response2 = urllib.request.urlopen(request2, timeout=5)
                    soup2 = BeautifulSoup(response2.read(),"html5lib")
                    for a1 in soup2.find_all(attrs={"class":'artists summary'}):
                        print ('http://www.songkick.com'+a1.a['href'])
                        link='http://www.songkick.com'+a1.a['href']
                        request3=urllib.request.Request(link)
                        response3 = urllib.request.urlopen(request3, timeout=5)
                        soup3 = BeautifulSoup(response3.read(),"html5lib")
                        document = NewDocument()
                        document.title = soup3.h1.span.string
                        document.description = soup3.find(attrs={"class":'additional-details-container'}).p.string
                        
                        document.date = soup3.h5.string
                        Loc=''
                        for span in soup2.find_all(attrs={"class":'location'}):
                            Loc += span.text
                        document.location = Loc
                        performer=''
                        for span in soup2.find_all(attrs={"class":'headliner'}):
                            performer += span.text                        
                        document.artists.append=(performer)
                        document.genres.append("")
                        document.tags.append("tag1")
                        document.tags.append("tag2")
                        document.tags.append("tag3")
                        document.urls.append(link)
                        document.imageUrls.append(soup3.find(attrs={"class": "profile-picture-wrapper"}).img['src'])
                        document.description = decomposeDocument(document.description);
                        document = multiLabelClassification(document);
                        document = clusterDocument(document);
                        document = findDuplicate(document);
                        document.save()
#                         print (a1.strong.string)
                        ft.write('http://www.songkick.com'+a1.a['href']+'\n')
                ft.close()




if __name__ == "__main__":  
    url = '.eventful.com/events?q=*&ga_search=*&ga_type=events&sort_order=Popularity&page_number='
    url1= 'http://www.songkick.com/session/filter_metro_area'
    request=urllib.request.Request(url)
    response = urllib.request.urlopen(request, timeout=5)
    #抓取页面内容
    soup = BeautifulSoup(response.read(),"html5lib")  
    s=soup.find(attrs={"class": "component popular-metro-areas"})
    for a in s.find_all('a'):
        location=a.string.split(',')[0].replace(' ','').lower()
        if (location=='sfbayarea'):
            location='sanfrancisco'
        else:
            if (location=='newyork'):
                location='newyorkcity'
        Sname=url.split('.')[1]+'\\'+location+'.txt'
#         Sname=url1.split('.')[1]+'\\'+location+'.txt'
        url1='http://www.songkick.com'+a['href']
        findDocuments(location,url,Sname)
#         findDocuments(lpcation,url1,Sname)
        

