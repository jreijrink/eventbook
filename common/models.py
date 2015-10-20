from django.db import models
from common.tokenizer import getTokensFromText
from common.tokenizer import getTokensFromList
import string

class NewDocument(object):

    def __init__(self):
        self.title = None
        self.description = None
        self.date = None
        self.location = None
        self.genres = list()
        self.artists = list()
        self.tags = list()
        self.urls = list()
        self.imageUrls = list()
    
        self.duplication = None
        
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
                TitleOrder.objects.create(token=titleToken, document=document)
            
            dateTokens = getTokensFromText(self.date)
            for date in dateTokens:
                dateToken = Token(date)
                dateToken.save()
                DateOrder.objects.create(token=dateToken, document=document)
                    
            locationTokens = getTokensFromText(self.location)
            for location in locationTokens:
                locationToken = Token(location)
                locationToken.save()
                LocationOrder.objects.create(token=locationToken, document=document)
                
            genreTokens = getTokensFromList(self.genres)
            for genre in genreTokens:
                genreToken = Token(genre)
                genreToken.save()
                GenresOrder.objects.create(token=genreToken, document=document)
                
            artistTokens = getTokensFromList(self.artists)
            for artist in artistTokens:
                artistToken = Token(artist)
                artistToken.save()
                ArtistOrder.objects.create(token=artistToken, document=document)
                
            tagTokens = getTokensFromList(self.tags)
            for tag in tagTokens:
                tagToken = Token(tag)
                tagToken.save()
                TagOrder.objects.create(token=tagToken, document=document)
    
            for url in self.urls:
                urlUrl = Url(url)
                urlUrl.save()
                UrlOrder.objects.create(url=urlUrl, document=document)
                
            for imageUrl in self.imageUrls:
                imageUrlUrl = Url(imageUrl)
                imageUrlUrl.save()
                ImageOrder.objects.create(url=imageUrlUrl, document=document)
            
            document.save
    
    def merge(self):
        if self.duplication:
            
            if not self.duplication.description:
                self.duplication.description = self.description
            
            self.duplication.save()
            
            dateTokens = getTokensFromText(self.date)
            for date in dateTokens:
                dateToken = Token(date)
                dateToken.save()
                if not DateOrder.objects.filter(token=dateToken, document=self.duplication).exists():
                    DateOrder.objects.create(token=dateToken, document=self.duplication)
                    
            locationTokens = getTokensFromText(self.location)
            for location in locationTokens:
                locationToken = Token(location)
                locationToken.save()
                if not LocationOrder.objects.filter(token=locationToken, document=self.duplication).exists():
                    LocationOrder.objects.create(token=locationToken, document=self.duplication)
                
            genreTokens = getTokensFromList(self.genres)
            for genre in genreTokens:
                genreToken = Token(genre)
                genreToken.save()
                if not GenresOrder.objects.filter(token=genreToken, document=self.duplication).exists():
                    GenresOrder.objects.create(token=genreToken, document=self.duplication)
                
            artistTokens = getTokensFromList(self.artists)
            for artist in artistTokens:
                artistToken = Token(artist)
                artistToken.save()
                if not ArtistOrder.objects.filter(token=artistToken, document=self.duplication).exists():
                    ArtistOrder.objects.create(token=artistToken, document=self.duplication)
                
            tagTokens = getTokensFromList(self.tags)
            for tag in tagTokens:
                tagToken = Token(tag)
                tagToken.save()
                if not TagOrder.objects.filter(token=tagToken, document=self.duplication).exists():
                    TagOrder.objects.create(token=tagToken, document=self.duplication)
    
            for url in self.urls:
                urlUrl = Url(url)
                urlUrl.save()
                if not UrlOrder.objects.filter(url=urlUrl, document=self.duplication).exists():
                    UrlOrder.objects.create(url=urlUrl, document=self.duplication)
                
            for imageUrl in self.imageUrls:
                imageUrlUrl = Url(imageUrl)
                imageUrlUrl.save()
                if not ImageOrder.objects.filter(url=imageUrlUrl, document=self.duplication).exists():
                    ImageOrder.objects.create(url=imageUrlUrl, document=self.duplication)
            
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
    title = models.ManyToManyField(Token, related_name='title_tokens', through='TitleOrder')
    
    description = models.CharField(max_length=1000)
    
    date = models.ManyToManyField(Token, related_name='date_tokens', through='DateOrder')
    location = models.ManyToManyField(Token, related_name='location_tokens', through='LocationOrder')
    
    genres = models.ManyToManyField(Token, related_name='genres_tokens', through='GenresOrder')
    artists = models.ManyToManyField(Token, related_name='artist_tokens', through='ArtistOrder')
    tags = models.ManyToManyField(Token, related_name='tag_tokens', through='TagOrder')
    
    urls = models.ManyToManyField(Url, related_name='url_urls', through='UrlOrder')
    imageUrls = models.ManyToManyField(Url, related_name='image_urls', through='ImageOrder')

    def __str__(self):
        return string.capwords(' '.join([str(title.name) for title in self.title.order_by("title_tokens")]))
    
    def getDate(self):
        return string.capwords(' '.join([str(date.name) for date in self.date.order_by("date_tokens")]))
    
    def getLocation(self):
        return string.capwords(' '.join([str(location.name) for location in self.location.order_by("location_tokens")]))
    
    def getGenres(self):
        return string.capwords(' / '.join([str(genres.name) for genres in self.genres.order_by("genres_tokens")]))
    
    def getArtists(self):
        return string.capwords(' / '.join([str(artists.name) for artists in self.artists.order_by("artist_tokens")]))
    
    
class TitleOrder(models.Model):
    token = models.ForeignKey(Token)
    document = models.ForeignKey(Document)
    
class DateOrder(models.Model):
    token = models.ForeignKey(Token)
    document = models.ForeignKey(Document)
    
class LocationOrder(models.Model):
    token = models.ForeignKey(Token)
    document = models.ForeignKey(Document)
    
class GenresOrder(models.Model):
    token = models.ForeignKey(Token)
    document = models.ForeignKey(Document)
    
class ArtistOrder(models.Model):
    token = models.ForeignKey(Token)
    document = models.ForeignKey(Document)
    
class TagOrder(models.Model):
    token = models.ForeignKey(Token)
    document = models.ForeignKey(Document)
    
class UrlOrder(models.Model):
    url = models.ForeignKey(Url)
    document = models.ForeignKey(Document)
    
class ImageOrder(models.Model):
    url = models.ForeignKey(Url)
    document = models.ForeignKey(Document)
    