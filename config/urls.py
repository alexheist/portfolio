from blog.models import Article
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, reverse
from django.utils import timezone
from markdownx import urls as markdownx

from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": GenericSitemap(
        {
            "queryset": Article.objects.filter(published__lte=timezone.now().date()),
            "date_field": "updated",
        },
        priority=0.9,
    ),
}

urlpatterns = [
    path("", include("main.urls")),
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("markdownx/", include(markdownx)),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
