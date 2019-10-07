from rest_framework import serializers
from . import models

class LeadSerializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.DateTimeField(
        format = "%m/%d/%Y (%I:%M %p)",
        required = False,
    )

    class Meta:
        model = models.Lead
        fields = [
            'url',
            'name',
            'email',
            'message',
            'timestamp',
        ]
