from django.urls import path
from .views import ListContactView

urlpatterns = [
	path('view/', ListContactView.as_view(), name='contact-all'),
]
