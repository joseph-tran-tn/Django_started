from django.shortcuts import HttpResponse

def index(request):
  return HttpResponse("Hello, this is the polls index. back to <a href='/'>Home</a>")
# Create your views here.
