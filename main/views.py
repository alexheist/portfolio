from blog import models as blog_models
from django import http
from django.shortcuts import render

from . import forms, models


def index(request):
    popular, recent = blog_models.Article.get_preview_articles()
    if request.is_ajax():
        # name = request.POST["name"]
        # email = request.POST["email"]
        # message = request.POST["message"]
        # y = request.POST
        # x = models.Lead.objects.create(name=name, email=email, message=message)
        form = forms.LeadForm(request.POST)
        if form.is_valid():
            form.save()
            # return http.JsonResponse({"status": "created"})
            return http.HttpResponse(status=200)
        return http.HttpResponse(status=400)
    return render(request, "main/index.html", {"popular": popular, "recent": recent})
