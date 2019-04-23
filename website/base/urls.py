from django.urls import path
from .views import (
	HomeView, ContactView, ThankYouView,
)

urlpatterns = [
	path('', HomeView.as_view()),
	path('contact/', ContactView.as_view(fields=['name', 'subject', 'phone', 'email', 'message'])),
	path('contact/thank-you', ThankYouView.as_view()),
]
