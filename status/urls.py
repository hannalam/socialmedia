from django.urls import path

# I wrote this code

from . import views

# the new posts/status urls
urlpatterns = [
    path('newpost', views.create_status, name='newpost'),
    path('main', views.main, name='main'),
    path('likes', views.main, name='likes'),
]

# end of code I wrote
