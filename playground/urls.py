from django.urls import path
from . import views

#Url Configuration
#mapping Url function to views
urlpatterns= [
    path('hello/', views.say_hello)
]

urlpatterns= [
    path('hello/', views.say_hello2)
]