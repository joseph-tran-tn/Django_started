from django.shortcuts import HttpResponse

def home(request):
  return HttpResponse("Hello, this is the home page")
