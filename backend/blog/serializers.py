from rest_framework import serializers
from . import models

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField()
    published = serializers.DateField(
        format = "%m/%d/%Y",
        required = False,
    )
    updated = serializers.DateField(
        format = "%m/%d/%Y",
        required = False,
    )

    class Meta:
        model = models.Article
        fields = (
            'url',
            'id',
            'author',
            'title',
            'markdown',
            'thumbnail',
            'slug',
            'published',
            'updated',
        )

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Author
        fields = (
            'url',
            'name_first',
            'name_last',
            'brief',
            'bio',
        )

class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Social
        fields = (
            'author',
            'platform',
            'url',
        )
