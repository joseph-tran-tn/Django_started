from django import forms
from django.forms.widgets import Textarea


class Contact_Form(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    subject = forms.CharField(max_length=25)
    body = forms.CharField(widget=Textarea)

# SHOW AUTOMATICALLY FORM
# from .models import ContactForm


# class Contact_Form(forms.ModelForm):
#     class Meta:
#         model = ContactForm
#         fields = ['username', 'email', 'subject', 'body']
