

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('services/', views.services, name='services'), 
    path('pricing/', views.pricing, name='pricing'), 
    path('contact/', views.contact, name='contact'), 
    path('about/', views.about, name='about'),        
   
]

