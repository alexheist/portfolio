import json
import urllib

from django import http
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from website.base import models, forms

class HomeView(TemplateView):
	template_name = 'pages/index.html'

class ContactView(TemplateView):
	template_name = 'pages/contact.html'
	form_class = forms.ContactForm
	success_url = '/contact/thank-you'

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		data['form'] = self.form_class
		return data

	def post(self, request):
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response,
		}
		data = urllib.parse.urlencode(values).encode()
		req = urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		if result['success']:
			form.save()
			return http.HttpResponseRedirect(self.success_url)
		else:
			#TODO: fix response failure
			messages.error(request, 'Invalid reCAPTCHA. Please try again.')
			return http.HttpResponse(messages.error, status=400)

class ThankYouView(TemplateView):
	template_name = 'pages/thank_you.html'
