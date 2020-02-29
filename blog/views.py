from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from better_profanity.profanity import contains_profanity

from . import models


def index(request):
    articles = models.Article.objects.filter(published__lte=timezone.now()).order_by(
        "-published"
    )
    return render(request, "blog/index.html", {"articles": articles})


def article(request, slug):
    article = get_object_or_404(models.Article, slug=slug)
    if request.is_ajax():
        article.hits += 1
        article.save()
        if request.method == "POST":
            appropriate = True
            name = request.POST.get("name")
            message = request.POST.get("message")
            if contains_profanity(name) or contains_profanity(message):
                appropriate = False
            models.Comment.objects.create(
                article=article, name=name, message=message, appropriate=appropriate
            )
    return render(request, "blog/article.html", {"article": article})


def comment_partial(request, slug):
    article = get_object_or_404(models.Article, slug=slug)
    return render(request, "partials/comment.html", {"article": article})
