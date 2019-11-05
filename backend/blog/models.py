from django.db import models
from django.utils import timezone

class Author(models.Model):
    name_first = models.CharField(max_length=31)
    name_last = models.CharField(max_length=31)
    brief = models.CharField(max_length=280, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

class Social(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    platform = models.CharField(max_length=31)
    url = models.CharField(max_length=255)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.CharField(max_length=127)
    thumbnail = models.ImageField()
    markdown = models.TextField()
    published = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)
    hits = models.IntegerField()
