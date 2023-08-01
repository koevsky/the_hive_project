from django.test import TestCase
from django.urls import reverse

from accounts.models import HiveUser
from cart_app.models import Cart


class UserLogoutViewTests(TestCase):

    VALID_USER_CRAETION_DATA = {
        'username': 'testname',
        'email': 'test@mail.com',
        'password': 'testpassword'
    }

    VALID_LOGIN_DATA = {
        'username': 'testname',
        'password': 'testpassword'
    }

    def setUp(self):

        self.user = HiveUser.objects.create_user(**self.VALID_USER_CRAETION_DATA)
        Cart.objects.create(user=self.user)

        self.logout_url = reverse('logout')
        self.index_url = reverse('index')

    def test_authenticated_user_logout(self):

        self.client.login(**self.VALID_LOGIN_DATA)
        response = self.client.get(self.logout_url)

        self.assertRedirects(response, self.index_url)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_unauthenticated_user_logout(self):
        response = self.client.get(self.logout_url)

        self.assertRedirects(response, self.index_url)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
