from django import forms

from website.base import models

from captcha import fields, widgets

class ContactForm(forms.ModelForm):
	recaptcha = fields.ReCaptchaField(
		widget = widgets.ReCaptchaV2Checkbox()
	)

	class Meta:
		model = models.Contact
		exclude = ['timestamp']
