from django.test import TestCase
from django.contrib.auth.models import Group
from django.urls import reverse
from accounts.models import HiveUser
from apiary_app.forms import ApiaryForm
from apiary_app.models import ApiaryModel
from cart_app.models import Cart


class ApiaryEditTests(TestCase):

    VALID_FORM_DATA = {
        'apiary_name': 'Testname',
        'location': 'Testtown',
        'hives_count': 5,
        'apiary_photo': '',
        'description': 'Testdescription'
    }

    VALID_USER_DATA = {
        'username': 'testname',
        'email': 'test@mail.com',
        'password': 'testpass123'
    }

    VALID_USER_DATA_UNAUTHORIZED = {
        'username': 'testname2',
        'email': 'test2@mail.com',
        'password': 'testpass123'
    }

    ORDINARY_LOGIN_DATA = {
        'username': 'testname',
        'password': 'testpass123'
    }

    LOGIN_DATA_UNAUTHORIZED = {
        'username': 'testunauth',
        'password': 'testpass123'
    }

    MODERATOR_LOGIN = {
        'username': 'moderator_test_user',
        'password': 'testpass123'
    }

    ADMIN_LOGIN = {
        'username': 'admin_test_user',
        'password': 'testpass123'
    }

    def setUp(self) -> None:

        self.ordinary_user = HiveUser.objects.create_user(**self.VALID_USER_DATA)
        Cart.objects.create(user=self.ordinary_user)

        self.unauthorized_user = HiveUser.objects.create_user(**self.VALID_USER_DATA_UNAUTHORIZED)
        Cart.objects.create(user=self.unauthorized_user)

        moderator_user_data = {**self.VALID_USER_DATA, 'username': 'moderator_test_user', 'email': 'testmoderator@mail.com'}
        self.moderator_user = HiveUser.objects.create_user(**moderator_user_data)
        Cart.objects.create(user=self.moderator_user)
        moderator_group = Group.objects.create(name='Moderator')
        self.moderator_user.groups.add(moderator_group)

        admin_user_data = {**self.VALID_USER_DATA, 'username': 'admin_test_user', 'email': 'testadmin@mail.com'}
        self.admin_user = HiveUser.objects.create_user(**admin_user_data)
        Cart.objects.create(user=self.admin_user)
        admin_group = Group.objects.create(name='Admin')
        self.admin_user.groups.add(admin_group)

        valid_apiary_data = {**self.VALID_FORM_DATA, 'owner': self.ordinary_user}
        self.apiary = ApiaryModel.objects.create(**valid_apiary_data)
        self.apiary_url = reverse('edit-apiary', kwargs={'pk': self.apiary.pk})

    def test_authorized_user_access_edit(self):

        self.client.login(**self.ORDINARY_LOGIN_DATA)
        response = self.client.get(self.apiary_url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ApiaryForm)

    def test_admin_access_edit(self):

        self.client.login(**self.ADMIN_LOGIN)
        response = self.client.get(self.apiary_url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ApiaryForm)

    def test_moderator_access_edit(self):

        self.client.login(**self.MODERATOR_LOGIN)
        response = self.client.get(self.apiary_url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ApiaryForm)

    def test_unauthorized_access_edit(self):

        self.client.login(**self.LOGIN_DATA_UNAUTHORIZED)
        response = self.client.get(self.apiary_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_success_apiary_edit_valid_data_auth_user(self):

        self.client.login(**self.ADMIN_LOGIN)
        new_apiary_data = {**self.VALID_FORM_DATA, 'apiary_name': 'Newtestname'}
        response = self.client.post(self.apiary_url, new_apiary_data)
        redirect_url = reverse('details-apiary', kwargs={'pk': self.apiary.pk})

        self.assertEqual(response.url, redirect_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_apiary_edit_invalid_data_auth_user(self):

        self.client.login(**self.MODERATOR_LOGIN)
        new_apiary_data = {**self.VALID_FORM_DATA, 'apiary_name': 'new+testname'}
        response = self.client.post(self.apiary_url, new_apiary_data)

        errors_text = response.context['form'].errors.as_text()

        self.assertIn('Name must consist of letters, digits or white space!', errors_text)
        self.assertIn('Name must start with uppercase latter!', errors_text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ApiaryForm)

