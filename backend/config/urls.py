import leads.views
import blog.views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'leads', leads.views.LeadViewSet)
router.register(r'articles', blog.views.ArticleViewSet)
router.register(r'authors', blog.views.AuthorViewSet)
router.register(r'published', blog.views.PublishedArticles, basename='published')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
