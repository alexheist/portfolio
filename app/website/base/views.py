from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.conf import settings
from website.base import models, forms

class HomeView(TemplateView):
	template_name = 'base/pages/index.html'

class ContactView(CreateView):
	template_name = 'base/pages/contact.html'
	form_class = forms.ContactForm

	success_url = '/contact/thank-you'

class ThankYouView(TemplateView):
	template_name = 'base/pages/thank_you.html'
