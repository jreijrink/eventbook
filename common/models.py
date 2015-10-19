from django.db import models
from common.tokenizer import getTokensFromText
from common.tokenizer import getTokensFromList

class NewDocument(object):
    title = None
    description = None
    date = None
    location = None
    genres = list()
    artists = list()
    tags = list()
    urls = list()
    imageUrls = list()
    
    duplication = None
        
    def save(self, *args, **kwargs):

        if self.duplication:
            self.merge()
        else:
            document = Document()
            
            document.description = self.description
            
            document.save()
            
            titleTokens = getTokensFromText(self.title)
            for title in titleTokens:
                titleToken = Token(title)
                titleToken.save()
                document.title.add(titleToken)
            
            dateTokens = getTokensFromText(self.date)
            for date in dateTokens:
                dateToken = Token(date)
                dateToken.save()
                document.date.add(dateToken)
                    
            locationTokens = getTokensFromText(self.location)
            for location in locationTokens:
                locationToken = Token(location)
                locationToken.save()
                document.location.add(locationToken)
                
            genreTokens = getTokensFromList(self.genres)
            for genre in genreTokens:
                genreToken = Token(genre)
                genreToken.save()
                document.genres.add(genreToken)
                
            artistTokens = getTokensFromList(self.artists)
            for artist in artistTokens:
                artistToken = Token(artist)
                artistToken.save()
                document.artists.add(artistToken)
                
            tagTokens = getTokensFromList(self.tags)
            for tag in tagTokens:
                tagToken = Token(tag)
                tagToken.save()
                document.tags.add(tagToken)
    
            for url in self.urls:
                urlUrl = Url(url)
                urlUrl.save()
                document.urls.add(urlUrl)
                
            for imageUrl in self.imageUrls:
                imageUrlUrl = Url(imageUrl)
                imageUrlUrl.save()
                document.imageUrls.add(imageUrlUrl)
            
            document.save
    
    def merge(self):
        if self.duplication:
            
            if not self.duplication.description:
                self.duplication.description = self.description
            
            self.duplication.save()
            
            titleTokens = getTokensFromText(self.title)
            for title in titleTokens:
                titleToken = Token(title)
                titleToken.save()
                self.duplication.title.add(titleToken)
            
            dateTokens = getTokensFromText(self.date)
            for date in dateTokens:
                if not self.duplication.date.filter(name=date).exists():
                    dateToken = Token(date)
                    dateToken.save()
                    self.duplication.date.add(dateToken)
                    
            locationTokens = getTokensFromText(self.location)
            for location in locationTokens:
                if not self.duplication.location.filter(name=location).exists():
                    locationToken = Token(location)
                    locationToken.save()
                    self.duplication.location.add(locationToken)
                
            genreTokens = getTokensFromList(self.genres)
            for genre in genreTokens:
                if not self.duplication.genres.filter(name=genre).exists():
                    genreToken = Token(genre)
                    genreToken.save()
                    self.duplication.genres.add(genreToken)
                
            artistTokens = getTokensFromList(self.artists)
            for artist in artistTokens:
                if not self.duplication.artists.filter(name=artist).exists():
                    artistToken = Token(artist)
                    artistToken.save()
                    self.duplication.artists.add(artistToken)
                
            tagTokens = getTokensFromList(self.tags)
            for tag in tagTokens:
                if not self.duplication.tags.filter(name=tag).exists():
                    tagToken = Token(tag)
                    tagToken.save()
                    self.duplication.tags.add(tagToken)
    
            for url in self.urls:
                if not self.duplication.urls.filter(name=url).exists():
                    urlUrl = Url(url)
                    urlUrl.save()
                    self.duplication.urls.add(urlUrl)
                
            for imageUrl in self.imageUrls:
                if not self.duplication.imageUrls.filter(name=imageUrl).exists():
                    imageUrlUrl = Url(imageUrl)
                    imageUrlUrl.save()
                    self.duplication.imageUrls.add(imageUrlUrl)
            
            self.duplication.save
            
    
class Token(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.name


class Url(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.ManyToManyField(Token, related_name='title_tokens')
    
    description = models.CharField(max_length=1000)
    
    date = models.ManyToManyField(Token, related_name='date_tokens')
    location = models.ManyToManyField(Token, related_name='location_tokens')
    
    genres = models.ManyToManyField(Token, related_name='genres_tokens')
    artists = models.ManyToManyField(Token, related_name='artist_tokens')
    tags = models.ManyToManyField(Token, related_name='tag_tokens')
    
    urls = models.ManyToManyField(Url, related_name='url_urls')
    imageUrls = models.ManyToManyField(Url, related_name='image_urls')

    def __str__(self):
        return ' '.join([str(title.name) for title in self.title.order_by("title_tokens")])
    