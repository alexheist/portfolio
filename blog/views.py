from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

from . import models


def index(request):
    articles = models.Article.objects.filter(published__lte=timezone.now()).order_by(
        "-published"
    )
    return render(request, "blog/index.html", {"articles": articles})


def article(request, slug):
    article = get_object_or_404(models.Article, slug=slug)
    if request.is_ajax:
        article.hits += 1
        article.save()
    return render(request, "blog/article.html", {"article": article})
