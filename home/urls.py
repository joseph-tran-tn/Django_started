from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blogDetail, name='blogDetail'),
    path('login-register/', views.loginRegister.as_view(), name='loginRegister'),
    path('member/', views.member, name='member'),
    path('logout/', views.logoutUser, name='logout'),
    path('poll/', views.poll, name='poll'),
]
