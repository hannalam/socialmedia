# I wrote this code

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, FriendList
from .forms import UserEditForm, ProfileEditForm, FriendListForm, SearchForm
from status.models import Status

from rest_framework import viewsets
from .serializers import ProfileSerializer, FriendListSerializer


# User login view with a form of login and password input
def user_login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                status = Status.objects.all()
                # when user login, redirect to the web homepage
                return render(request, 'status/main.html', {'status': status})
            else:
                return HttpResponse('Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


# after login, the homepage contain the user photo and status
@login_required
def home(request):
    loggedin_user = request.user
    status = Status.objects.filter(user=loggedin_user)
    profile = Profile.objects.filter(user=loggedin_user).first()
    return render(request, 'users/home.html', {'status': status, 'profile': profile})


# user can register in this page
def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


# user can edit their profile after login
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('main')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {'user_form': user_form, 'profile_form': profile_form})


# user can add friend and create a nickname in the friendlist page for them after login
@login_required
def friendlist(request):
    loggedin_user = request.user
    newfriend = FriendList.objects.all()
    friend_form = FriendListForm(instance=request.user)
    if friend_form.is_valid():
        return redirect('main')
    return render(request, 'users/friendlist.html', {'newfriend': newfriend, 'friend_form': friend_form})


# search a friend
def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Profile.objects.filter(name__icontains=query)
            return render(request, 'search_results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'friendlist.html', {'form': form})

# prfile serialize for api setup


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# friend list serialize for api setup
class FriendListViewSet(viewsets.ModelViewSet):
    queryset = FriendList.objects.all()
    serializer_class = FriendListSerializer

# end of code I wrote
