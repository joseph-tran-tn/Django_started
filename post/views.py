from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Post");

def post1(request):
    return HttpResponse("Post1");
def post2(request):
    return HttpResponse("Post2");
