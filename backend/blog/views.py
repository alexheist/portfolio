from rest_framework import (
    authentication,
    permissions,
    viewsets
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

class SocialViewSet(viewsets.ModelViewSet):
    authentication_classes = (
        authentication.SessionAuthentication,
    )
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Social.objects.all().order_by('-author__name_last')
    serializer_class = serializers.SocialSerializer
