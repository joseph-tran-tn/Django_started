from django.http.response import HttpResponse
from django.shortcuts import render
from .models import PostForm
from .forms import RegisterForm, LoginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home/index.html')


def blog(request):
    pF = PostForm.objects.all()
    return render(request, 'home/blog/index.html', {'blogs': pF})


def blogDetail(request, id):
    pD = PostForm.objects.get(id=id)
    return render(request, 'home/blog/detail.html', {'blog': pD})


class loginRegister(View):
    def get(self, request):
        context = {
            'RegisterForm': RegisterForm,
            'LoginForm': LoginForm
        }
        return render(request, 'home/login-register/index.html', context)

    def post(self, request):
        if 'register' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            return HttpResponse('Register successfully')
        else:
            username = request.POST['emailOrUsername']
            password = request.POST['password']
            try:
                emailByUser = User.objects.get(email=username)
                user = authenticate(
                    request,
                    username=emailByUser,
                    password=password
                )
            except:
                user = authenticate(
                    request,
                    username=username,
                    password=password
                )
            if user is not None:
                login(request, user)
                return redirect('/member/')
            else:
                return HttpResponse('Login failed')


@login_required
def member(request):
    return render(request, 'home/member/index.html')


def logoutUser(request):
    logout(request)
    return redirect('/')


def poll(request):
    return render(request, 'home/poll/index.html')
