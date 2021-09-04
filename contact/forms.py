from django import forms
from .models import ContactForm


class Contact_Form(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['username', 'email', 'subject', 'body']
