from django.test import TestCase
from django.urls import reverse

from accounts.models import HiveUser
from cart_app.models import Cart


class UserProfileDetailsViewTest(TestCase):

    VALID_USER_CREATION_DATA = {
        'username': 'testusername',
        'email': 'test@mail.com',
        'password': 'testpass123',
    }

    VALID_LOGIN_DATA = {
        'username': 'testusername',
        'password': 'testpass123',
    }

    def setUp(self):

        self.user = HiveUser.objects.create_user(**self.VALID_USER_CREATION_DATA)
        Cart.objects.create(user=self.user)

        self.profile_details_url = reverse('profile-details', kwargs={'pk': self.user.pk})
        self.index_url = reverse('index')
        self.login_url = reverse('login')

    def test_authenticated_user_profile_details(self):

        self.client.login(**self.VALID_LOGIN_DATA)
        response = self.client.get(self.profile_details_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_user'])
        self.assertTrue(response.context['is_auth'])
        self.assertFalse(response.context['is_admin'])
        self.assertFalse(response.context['is_moderator'])

    def test_unauthenticated_user_profile_details(self):

        response = self.client.get(self.profile_details_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={self.profile_details_url}')

    def test_invalid_pk_profile_details_authenticated_user(self):

        self.client.login(**self.VALID_LOGIN_DATA)
        invalid_profile_url = reverse('profile-details', kwargs={'pk': 9999})
        response = self.client.get(invalid_profile_url)

        self.assertEqual(response.status_code, 404)


