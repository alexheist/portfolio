from django.db import models
from django.utils import timezone


class Lead(models.Model):
    name = models.CharField(max_length=31)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)

    def __str__(self):
        year = self.timestamp.year
        month = self.timestamp.month
        day = self.timestamp.day
        hour = self.timestamp.hour
        minute = self.timestamp.minute
        return f"{year}-{month}-{day} ({hour}:{minute})| {self.email} | {self.message[:60]}"
