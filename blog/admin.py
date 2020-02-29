from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from . import models


@admin.register(models.Article)
class ArticleAdmin(MarkdownxModelAdmin):
    list_display = ("title", "slug", "hits", "published", "updated")
    date_heirarchy = "published"
