from django import forms
from website.base import models

class ContactForm(forms.ModelForm):
	class Meta:
		model = models.Contact
		exclude = ['timestamp']
