from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blogDetail, name='blogDetail'),
    path('poll/', views.poll, name='poll'),
]
