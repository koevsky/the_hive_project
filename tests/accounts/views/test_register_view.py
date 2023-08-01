from django.test import TestCase
from django.urls import reverse
from accounts.models import HiveUser
from cart_app.models import Cart


class UserRegisterViewTest(TestCase):

    VALID_USER_REGISTER_DATA = {
        'username': 'testusername',
        'email': 'testmail@mail.com',
        'password1': 'testpass123',
        'password2': 'testpass123'
    }

    VALID_USER_LOGIN_DATA = {
        'username': 'testusername',
        'password': 'testpass123',
    }

    def setUp(self):

        self.register_url = reverse('register')
        self.index_url = reverse('index')

    def test_register_with_valid_data(self):

        response = self.client.post(self.register_url, self.VALID_USER_REGISTER_DATA)
        user = HiveUser.objects.filter(username='testusername').first()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.index_url)
        self.assertTrue(HiveUser.objects.filter(username='testusername').exists())
        self.assertTrue(Cart.objects.filter(user=user).exists())

    def test_register_with_invalid_data(self):

        invalid_data = {**self.VALID_USER_REGISTER_DATA, 'email': 'wrongmailtest'}

        response = self.client.post(self.register_url, invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(HiveUser.objects.filter(username='testusername').exists())

    def test_register_with_authenticated_user(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_LOGIN_DATA)
        Cart.objects.create(user=user)
        self.client.login(**self.VALID_USER_LOGIN_DATA)

        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.index_url)

