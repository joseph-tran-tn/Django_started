from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
  path('', views.index, name='index'),
  path('blog/', views.blog, name='blog'),
  path('poll/', views.poll, name='poll'),
]
