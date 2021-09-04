from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import Contact_Form
from .models import ContactForm
# Create your views here.


def index(request):
    context = {'Contact_Form': Contact_Form}
    return render(request, 'contact/index.html', context)


def saveContact(request):
    if request.method == 'POST':
        cf = Contact_Form(request.POST)
        if cf.is_valid():
            saveCF = ContactForm(
                username=cf.cleaned_data['username'],
                email=cf.cleaned_data['email'],
                subject=cf.cleaned_data['subject'],
                body=cf.cleaned_data['body'],
            )
            saveCF.save()
            return render(request, 'contact/success.html')
        else:
            return HttpResponse(cf.errors)
    else:
        return HttpResponse('not POST')
# SHOW AUTOMATICALLY FORM
# return render(request, 'contact/index.html', context)
# def getContact(request):
#     if request.method == "POST":
#         cf = Contact_Form(request.POST)
#         if cf.is_valid():
#             cf.save()
#             return HttpResponse('Save success')
#     else:
#         return HttpResponse('not POST')
