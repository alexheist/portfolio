from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Article(models.Model):
    title = models.CharField(max_length=63)
    description = models.CharField(max_length=160)
    slug = models.CharField(max_length=127, unique=True)
    markdown = MarkdownxField()
    published = models.DateField()
    updated = models.DateField(blank=True, null=True)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.published} | {self.title}"

    @property
    def formatted_markdown(self):
        return markdownify(self.markdown)
