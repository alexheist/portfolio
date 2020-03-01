from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog"),
    path("<str:slug>/", views.article, name="blog_detail"),
    path("<str:slug>/comments/", views.comment_partial, name="comment_partial"),
]
