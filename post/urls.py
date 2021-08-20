from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('1/', views.post1, name='post1'),
  path('2/', views.post2, name='post2'),
]
