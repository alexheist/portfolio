from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="main"),
]
