from django.shortcuts import render
from .models import PostForm


def index(request):
    return render(request, 'home/index.html')


def blog(request):
    pF = PostForm.objects.all()
    return render(request, 'home/blog/index.html', {'pF': pF})


def blogDetail(request, id):
    pD = PostForm.objects.get(id=id)
    return render(request, 'home/blog/detail.html', {'pD': pD})


def poll(request):
    return render(request, 'home/poll/index.html')
