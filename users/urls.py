# I wrote this code

from django.urls import path, include
from . import views
from re import template
from django.contrib.auth import views as auth_view

from rest_framework import routers
from users.views import ProfileViewSet, FriendListViewSet
from django.conf.urls.static import static
from django.conf import settings

# register for the REST API
router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('friends', FriendListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # password handling with change, reset
    path('password_change/', auth_view.PasswordChangeView.as_view(
        template_name='users/password_change_form.html'), name='password_change'),
    path('password_change/done', auth_view.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_view.PasswordResetView.as_view(
        template_name='users/password_reset_form.html'), name='password_reset'),
    path('password_reset/done', auth_view.PasswordChangeDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', auth_view.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    # user profile editing and friendllist
    path('edit/', views.edit, name='edit'),
    path('friendlist/', views.friendlist, name='friendlist'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # photos in the media files

# end of code I wrote
