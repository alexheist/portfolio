from django.db import models
from django.utils import timezone

class Author(models.Model):
    name_first = models.CharField(max_length=31)
    name_last = models.CharField(max_length=31)
    brief = models.CharField(max_length=280, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.name_last, self.name_first)

class Social(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    platform = models.CharField(max_length=31)
    url = models.CharField(max_length=255)

    def __str__(self):
        return '[{}]({})'.format(self.platform, self.url)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=63)
    slug = models.CharField(max_length=127)
    thumbnail = models.ImageField()
    markdown = models.TextField()
    published = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return '{} | {}'.format(self.published, self.title)

    def save(self, *args, **kwargs):
        self.slug = '{}/{}/{}'.format(
            self.published.year,
            self.published.month,
            self.slug
        )
        super(Article, self).save(*args, **kwargs)
