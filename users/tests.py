# I wrote this code

from django.test import TestCase, Client
from users.models import Profile
from django.urls import reverse
from users.forms import UserRegistrationForm
from rest_framework.test import APITestCase


# Testing Models
class ProfileModelTestCase(TestCase):
    def test_profile_str(self):
        user = Profile.objects.create(
            username='testuser', photo='190073344.jpg')
        self.assertEqual(str(user), 'testuser')


# Testing Views
class UserProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Profile.objects.create(
            username='testuser', photo='190073344.jpg')

    def test_user_view(self):
        response = self.client.get(reverse('user', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')


# Testing Forms
class UserRegistrationFormTestCase(TestCase):
    def test_password_match(self):
        form_data = {'username': 'user',
                     'password': 'user1234', 'password2': 'user1234'}
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        form_data = {'username': 'user',
                     'password': 'user1234', 'password2': 'user5678'}
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


# Testing API Views (using Django REST framework)
class ProfileAPITestCase(APITestCase):
    def setUp(self):
        self.user = Profile.objects.create(
            username='testuser', photo='190073344.jpg')
        self.url = '/api/users/'

    def test_profile_api_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_profile_api_retrieve(self):
        response = self.client.get(f'{self.url}{self.user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')

# end of code I wrote
