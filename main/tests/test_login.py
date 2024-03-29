from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

#python manage.py test

class BaseTest(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.users_url = reverse('users')
        self.client = APIClient()
        self.user = User.objects.create_user('johnny', email='jb@gmail.com', password='j54321')
        self.user.save()

        return super().setUp()

class LoginTest(BaseTest):
    def test_can_access_login_page(self):
        response = self.client.get(self.login_url)
        # status: 405 , as does not allow to do a GET method
        self.assertEqual(response.status_code, 405)
        print()

    def test_login_sucess(self):
        # client data inputs
        self.user_credentials = {
            'username': 'johnny',
            'password': 'j54321'
        }
        request = self.client.post(self.login_url, self.user_credentials, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        print("Login Success!")
        print()

    def test_login_fail_username(self):
        # client data inputs
        self.user_credentials = {
            'username': 'johnny2',
            'password': 'j54321'
        }
        request = self.client.post(self.login_url, self.user_credentials, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        print("Login Fail, wrong username Success!")

    def test_login_fail_password(self):
        # client data inputs
        self.user_credentials = {
            'username': 'johnny',
            'password': 'j12345'
        }
        request = self.client.post(self.login_url, self.user_credentials, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        print("Login Fail, wrong password Success!")
        print()

    # able to access user's view
    def test_view_users(self):
        response = self.client.get(self.users_url)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        print("View users Success!")
        print()

    def test_login_success(self):
        # able to login
        self.assertTrue(self.client.login(username='johnny', password='j54321'))
        print("Login Successful")
        # able to access users
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, 200)
        print()