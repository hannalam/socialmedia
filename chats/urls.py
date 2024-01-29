from django.contrib import admin
from django.urls import path

# I wrote this code

from .import views

# chat room urls
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.chatroom, name='chatroom'),
]


# end of code I wrote
