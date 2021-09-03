from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def blog(request):
    return render(request, 'home/blog/index.html')

def poll(request):
    return render(request, 'home/poll/index.html')
