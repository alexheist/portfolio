from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

class ListContactView(generics.ListAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
