from django.db import models
from django.utils import timezone


class Lead(models.Model):
    name = models.CharField(max_length=31)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.localtime)
    seen = models.BooleanField(default=False)
    response = models.BooleanField(default=False)
