import requests
from better_profanity.profanity import contains_profanity
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from . import models


def index(request):
    articles = models.Article.objects.filter(published__lte=timezone.now()).order_by(
        "-published"
    )
    return render(request, "blog/index.html", {"articles": articles})


def check_recaptcha(token):
    data = {"secret": settings.RECAPTCHA_PRIVATE_KEY, "response": token}
    response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify", data=data
    )
    result = response.json()
    if result["success"] == True and result["score"] >= 0.6:
        return True
    return False


def check_profanity(name, message):
    if contains_profanity(name) or contains_profanity(message):
        return True
    return False


def article(request, slug):
    article = get_object_or_404(models.Article, slug=slug)
    if request.is_ajax():
        article.hits += 1
        article.save()
        if request.method == "POST":
            token = request.POST.get("recaptcha")
            name = request.POST.get("name")
            message = request.POST.get("message")
            appropriate = True
            if check_profanity(name, message) or not check_recaptcha(token):
                appropriate = False
            models.Comment.objects.create(
                article=article, name=name, message=message, appropriate=appropriate
            )
    return render(
        request,
        "blog/article.html",
        {"article": article, "recaptcha_key": settings.RECAPTCHA_PUBLIC_KEY},
    )


def comment_partial(request, slug):
    article = get_object_or_404(models.Article, slug=slug)
    return render(request, "partials/comment.html", {"article": article})
