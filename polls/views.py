from django.shortcuts import HttpResponse

def index(request):
  return HttpResponse("Hello, this is the polls index")
# Create your views here.
