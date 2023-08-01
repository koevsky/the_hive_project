from django.test import TestCase
from django.urls import reverse
from accounts.models import HiveUser
from cart_app.models import Cart


class UserLoginViewTest(TestCase):

    VALID_USER_CREATION_DATA = {
        'username': 'testusername',
        'email': 'test@mail.com',
        'password': 'testpass123',
    }

    def setUp(self):

        self.user = HiveUser.objects.create_user(**self.VALID_USER_CREATION_DATA)
        Cart.objects.create(user=self.user)

        self.login_url = reverse('login')
        self.index_url = reverse('index')

    def test_authenticated_user_access_login_page(self):
        self.client.login(**self.VALID_USER_CREATION_DATA)

        response = self.client.get(self.login_url)

        self.assertRedirects(response, self.index_url)
        self.assertEqual(response.status_code, 302)

    def test_unauthenticated_user_access_login_page(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_login(self):
        self.client.login(**self.VALID_USER_CREATION_DATA)

        response = self.client.get(self.login_url)

        self.assertRedirects(response, self.index_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_unauthenticated_user_login(self):

        new_data = {
            'username': 'testuser',
            'email': 'test12@mail.com',
            'password': 'testpassword1',
        }

        user = HiveUser.objects.create_user(**new_data)
        Cart.objects.create(user=user)

        response = self.client.post(self.login_url, new_data)

        self.assertRedirects(response, self.index_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_invalid_credentials(self):

        new_data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }

        response = self.client.post(self.login_url, new_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)