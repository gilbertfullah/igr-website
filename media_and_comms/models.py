from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class Release(models.Model):
    title = models.CharField(verbose_name="Title", max_length=250)
    content = RichTextField(null=True, blank=True)
    published_date = models.DateField(verbose_name="Published Date")
    author = models.CharField(verbose_name="Author", max_length=250)
    image = models.ImageField(verbose_name="Image", null=True, blank=True, upload_to="releases/")
    document = models.FileField(verbose_name="Document", null=True, blank=True)
    tags = TaggableManager(blank=True, related_name='release_tags')
    created_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Releases"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.CharField(verbose_name="Name", max_length=100)
    parent_post = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=255)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.author}: : {self.body[:30]}' 
    
class Reply(models.Model):
    author = models.CharField(verbose_name="Name", max_length=100)
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    body = models.CharField(max_length=150)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.author}: : {self.body[:30]}' 

    class Meta:
        ordering = ['-created_at']

class News(models.Model):
    title = models.CharField(verbose_name="Title", max_length=250)
    content = RichTextField(null=True, blank=True)
    published_date = models.DateField(verbose_name="Published Date")
    posted_by = models.CharField(verbose_name="Posted By", max_length=250)
    image = models.ImageField(verbose_name="Image", upload_to="news/")
    url = models.URLField()
    tags = TaggableManager(blank=True, related_name='news_tags')
    created_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "News"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
class Podcast(models.Model):
    title = models.CharField(verbose_name="Title", max_length=250)
    description = RichTextField(null=True, blank=True)
    published_date = models.DateField(verbose_name="Published Date")
    image = models.ImageField(verbose_name="Image", upload_to="podcast/")
    host = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Podcasts"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    title = models.CharField(verbose_name="Title", max_length=250)
    image = models.ImageField(upload_to='gallery/')
    
    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.title