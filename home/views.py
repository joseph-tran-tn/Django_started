from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the home page, <a href='./polls/'>Polls</a>")
