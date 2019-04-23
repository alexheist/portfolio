from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.conf import settings
from website.contact.models import Contact

class HomeView(TemplateView):
	template_name = 'pages/index.html'

class ContactView(CreateView):
	template_name = 'pages/contact.html'
	model = Contact
	exclude = ['timestamp']

	success_url = '/contact/thank-you'

class ThankYouView(TemplateView):
	template_name = 'pages/thank_you.html'
