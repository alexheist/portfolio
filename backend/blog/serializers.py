from rest_framework import serializers

from . import models


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    published = serializers.DateField(format="%m/%d/%Y", required=False,)
    updated = serializers.DateField(format="%m/%d/%Y", required=False,)

    class Meta:
        model = models.Article
        fields = (
            "url",
            "author",
            "title",
            "slug",
            "thumbnail",
            "markdown",
            "published",
            "updated",
        )


class PublishedSerializer(serializers.HyperlinkedModelSerializer):
    name_first = serializers.CharField(source="author.name_first")
    name_last = serializers.CharField(source="author.name_last")
    published = serializers.DateField(format="%m/%d/%Y", required=False,)
    updated = serializers.DateField(format="%m/%d/%Y", required=False,)

    class Meta:
        model = models.Article
        fields = (
            "name_first",
            "name_last",
            "title",
            "markdown",
            "thumbnail",
            "slug",
            "published",
            "updated",
            "hits",
        )
        depth = 1


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Author
        fields = (
            "url",
            "name_first",
            "name_last",
        )
