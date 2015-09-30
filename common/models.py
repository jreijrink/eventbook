from django.db import models
 
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
        
        titleTag = Tag(self.title)
        titleTag.save()
        document.title = titleTag
        
        document.description = self.description
        
        dateTag = Tag(self.date)
        dateTag.save()
        document.date = dateTag
        
        locationTag = Tag(self.location)
        locationTag.save()
        document.location = locationTag
        
        document.save()
        
        for genre in self.genres:
            genreTag = Tag(genre)
            genreTag.save()
            document.genres.add(genreTag)
            
        for artist in self.artists:
            artistTag = Tag(artist)
            artistTag.save()
            document.artists.add(artistTag)
            
        for tag in self.tags:
            tagTag = Tag(tag)
            tagTag.save()
            document.tags.add(tagTag)
            
        for url in self.urls:
            urlUrl = Url(url)
            urlUrl.save()
            document.urls.add(urlUrl)
            
        for imageUrl in self.imageUrls:
            imageUrlUrl = Url(imageUrl)
            imageUrlUrl.save()
            document.imageUrls.add(imageUrlUrl)
        
        document.save
    
class Tag(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.name


class Url(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.ForeignKey(Tag, related_name='title_tag')
    
    description = models.CharField(max_length=1000)
    
    date = models.ForeignKey(Tag, related_name='date_tags')
    location = models.ForeignKey(Tag, related_name='location_tag')
    
    genres = models.ManyToManyField(Tag, related_name='genres_tags')
    artists = models.ManyToManyField(Tag, related_name='artist_tags')
    tags = models.ManyToManyField(Tag, related_name='tag_tags')
    
    urls = models.ManyToManyField(Url, related_name='url_urls')
    imageUrls = models.ManyToManyField(Url, related_name='image_urls')

    def __str__(self):
        return self.title.name
    