from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=63)
    description = models.CharField(max_length=160)
    slug = models.CharField(max_length=127, unique=True)
    markdown = models.TextField()
    published = models.DateField()
    updated = models.DateField(blank=True, null=True)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.published} | {self.title}"
