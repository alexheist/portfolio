from django import forms
from . import models


class LeadForm(forms.ModelForm):
    class Meta:
        model = models.Lead
        fields = ("name", "email", "message")

