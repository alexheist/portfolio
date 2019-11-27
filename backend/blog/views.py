from rest_framework import (
    authentication,
    permissions,
    viewsets,
    response
)
from . import models, serializers

class AuthorViewSet(viewsets.ModelViewSet):
    authentication_classes = (
        authentication.SessionAuthentication,
    )
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Author.objects.all().order_by('-name_last')
    serializer_class = serializers.AuthorSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    authentication_classes = (
        authentication.SessionAuthentication,
    )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Article.objects.all().order_by('-published', '-id')
    serializer_class = serializers.ArticleSerializer

class ArticleBySlug(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        article = models.Article.objects.get(slug=pk)
        serializer = serializers.ArticleSerializer(article, context={'request': request})
        return response.Response(serializer.data)
