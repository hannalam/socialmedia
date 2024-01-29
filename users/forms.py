# I wrote this code

from django import forms
from django.contrib.auth.models import User
from .models import Profile, FriendList

# user edit form


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# profile edit form


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)

# login form


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# user registration form


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name'}

    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Password do not match')
        return self.cleaned_data['password2']

# friend list form


class FriendListForm(forms.ModelForm):
    class Meta:
        model = FriendList
        fields = {'user', 'nickname'}

# friend search form


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')


# end of code I wrote
