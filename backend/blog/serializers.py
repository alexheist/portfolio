from rest_framework import serializers
from . import models

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = '__all__'

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'

class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Social
        fields = '__all__'
