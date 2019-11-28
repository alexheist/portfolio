from django.utils import timezone
from rest_framework import (
    authentication,
    permissions,
    viewsets,
    response
)
from config import authentication as c_auth
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

class PublishedArticles(viewsets.ViewSet):
    authentication_classes = (c_auth.CsrfExemptSessionAuth,)
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = models.Article.objects.filter(
            published__lte = timezone.now().date(),
        ).order_by('-published', '-id')
        serializer = serializers.PublishedSerializer(
            queryset,
            many = True,
            context = {'request': request}
        )
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = models.Article.objects.get(slug=pk)
        serializer = serializers.PublishedSerializer(
            article,
            context = {'request': request}
        )
        return response.Response(serializer.data)

    def partial_update(self, request, pk=None):
        article = models.Article.objects.get(slug=request.data['article'])
        article.hits += 1
        article.save()
        return response.Response(status=200)
