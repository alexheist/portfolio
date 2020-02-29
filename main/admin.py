from django.contrib import admin

from . import models


def mark_seen(modeladmin, request, queryset):
    queryset.update(seen=True)


def mark_response(modeladmin, request, queryset):
    queryset.update(response=True)


mark_seen.short_description = "Mark leads as seen"
mark_response.short_description = "Leads were responded to"


@admin.register(models.Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "message", "timestamp", "seen", "response")
    date_heirarchy = "published"
    actions = (mark_seen, mark_response)


admin.site.site_header = "Welcome Back"
admin.site.site_title = "Alex Heist"
admin.site.index_title = "Admin"
