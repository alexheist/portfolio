from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Author(models.Model):
    name_first = models.CharField(max_length=31)
    name_last = models.CharField(max_length=31)

    def __str__(self):
        return f"{self.name_first} {self.name_last}"


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=63)
    slug = models.CharField(max_length=127, unique=True)
    thumbnail = models.ImageField()
    markdown = models.TextField()
    published = models.DateField()
    updated = models.DateField(blank=True, null=True)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.published} | {self.title}"


@receiver(post_save, sender=Article)
def create_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = (
            f"{instance.published.year}-{instance.published.month}-{instance.slug}"
        )
