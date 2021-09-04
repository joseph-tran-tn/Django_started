from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),
    path('save-contact/', views.saveContact, name='saveContact'),
    # SHOW AUTOMATICALLY FORM
    # path('get-contact/', views.getContact, name='getContact'),
]
