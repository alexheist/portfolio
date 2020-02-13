from django.shortcuts import render
from blog import models


def index(request):
    popular, recent = models.Article.get_preview_articles()
    return render(request, "main/index.html", {"popular": popular, "recent": recent})
