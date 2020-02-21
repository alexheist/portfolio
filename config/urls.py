from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from markdownx import urls as markdownx

urlpatterns = [
    path("", include("main.urls")),
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("markdownx/", include(markdownx)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
