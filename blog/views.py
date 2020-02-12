from django.shortcuts import render

from . import models


def index(request):
    articles = models.Article.objects.all().order_by("-published")[:6]
    return render(request, "blog/index.html", {"articles": articles})
