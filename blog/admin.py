from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from . import models


def mark_seen(modeladmin, request, queryset):
    queryset.update(seen=True)


def mark_appropriate(modeladmin, request, queryset):
    queryset.update(appropriate=True)


def mark_inappropriate(modeladmin, request, queryset):
    queryset.update(appropriate=False)


mark_seen.short_description = "Mark as seen"
mark_appropriate.short_description = "Mark as appropriate"
mark_inappropriate.short_description = "Mark as inappropriate"


@admin.register(models.Article)
class ArticleAdmin(MarkdownxModelAdmin):
    list_display = ("title", "slug", "hits", "published", "updated")
    date_heirarchy = "published"


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "article",
        "name",
        "message",
        "timestamp",
        "seen",
        "appropriate",
        "response",
    )
    actions = (mark_seen, mark_appropriate, mark_inappropriate)

