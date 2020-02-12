from django.shortcuts import render
from django.utils import timezone

from . import models


def index(request):
    articles = models.Article.objects.filter(published__lte=timezone.now()).order_by(
        "-published"
    )
    return render(request, "blog/index.html", {"articles": articles})
