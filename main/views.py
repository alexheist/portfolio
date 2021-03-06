from django import http
from django.shortcuts import render

from . import forms


def index(request):
    if request.is_ajax():
        form = forms.LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponse(status=200)
        return http.HttpResponse(status=400)
    return render(request, "main/index.html", {})
