from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
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
        return self.title

    @property
    def formatted_markdown(self):
        return markdownify(self.markdown)

    @property
    def comments(self):
        return self.comment_set.filter(appropriate=True).order_by("-timestamp")

    def get_preview_articles():
        current_date = timezone.localtime().date()
        articles = __class__.objects.filter(published__lte=current_date)
        popular = list(articles.order_by("-hits")).pop(0)
        recent = articles.order_by("-published").exclude(id=popular.id)[0]
        return popular, recent

    def get_absolute_url(self):
        return reverse("blog_detail", args=[str(self.slug)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    seen = models.BooleanField(default=False)
    response = models.TextField(blank=True, null=True)
    appropriate = models.BooleanField(default=True)

