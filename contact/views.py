from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import Contact_Form
# Create your views here.


def index(request):
    context = {'Contact_Form': Contact_Form}
    return render(request, 'contact/index.html', context)


def getContact(request):
    if request.method == "POST":
        cf = Contact_Form(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse('Save success')
    else:
        return HttpResponse('not POST')
