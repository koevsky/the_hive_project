from django.test import TestCase
from django.urls import reverse

from accounts.models import HiveUser
from apiary_app.forms import ApiaryForm
from apiary_app.models import ApiaryModel
from cart_app.models import Cart


class ApiaryCreateTests(TestCase):

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

    LOGIN_DATA = {

        'username': 'testname',
        'password': 'testpass123'

    }

    def setUp(self):

        self.user = HiveUser.objects.create_user(**self.VALID_USER_DATA)

        Cart.objects.create(user=self.user)
        self.success_url = reverse('profile-apiaries', kwargs={'pk': self.user.pk})

    def test_apiary_create_view_auth_user(self):

        self.client.login(**self.LOGIN_DATA)
        url = reverse('create-apiary')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'apiary/create_apiary.html')
        self.assertIsInstance(response.context['form'], ApiaryForm)

    def test_apiary_create_view_unauth_user(self):

        url = reverse('create-apiary')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?next=' + url)

    def test_apiary_create_view_form_valid(self):

        self.client.login(**self.LOGIN_DATA)
        url = reverse('create-apiary')
        valid_data = {**self.VALID_FORM_DATA, 'owner': self.user}
        response = self.client.post(url, valid_data)
        apiary = ApiaryModel.objects.filter(apiary_name='Testname', owner=self.user)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(apiary.exists())
        self.assertRedirects(response, reverse('profile-apiaries', kwargs={'pk': self.user.pk}))

    def test_apiary_create_view_form_invalid(self):

        self.client.login(**self.LOGIN_DATA)
        url = reverse('create-apiary')
        invalid_form_data = {**self.VALID_FORM_DATA, 'apiary_name': 'testname'}
        response = self.client.post(url, invalid_form_data)
        apiary = ApiaryModel.objects.filter(apiary_name='testname', owner=self.user)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(apiary.exists())
        self.assertTemplateUsed(response, 'apiary/create_apiary.html')






