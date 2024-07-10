from django.urls import path, include
from .views import*
# from views import home
from app import views

urlpatterns = [
    path('home/',views.home ,name='home')
]
    
