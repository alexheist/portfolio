from rest_framework import serializers
from . import models

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.StringRelatedField()
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
            'author_name',
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
        )
