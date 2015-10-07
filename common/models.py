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
    
    def save(self, *args, **kwargs):
        
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
    