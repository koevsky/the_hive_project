from django.test import TestCase
from django.urls import reverse

from accounts.models import HiveUser
from apiary_app.models import ApiaryModel
from cart_app.models import Cart


class ApiaryDetailsViewTests(TestCase):

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

    def setUp(self) -> None:

        self.user = HiveUser.objects.create_user(**self.VALID_USER_DATA)
        Cart.objects.create(user=self.user)
        valid_data = {**self.VALID_FORM_DATA, 'owner': self.user}
        self.apiary = ApiaryModel.objects.create(**valid_data)

        self.apiary_details_url = reverse('details-apiary', kwargs={'pk': self.apiary.pk})

        self.index_url = reverse('index')
        self.login_url = reverse('login')


    def test_authenticated_user_apiary_details(self):

        self.client.login(**self.LOGIN_DATA)
        response = self.client.get(self.apiary_details_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_user'])
        self.assertTrue(response.context['is_auth'])
        self.assertFalse(response.context['is_admin'])
        self.assertFalse(response.context['is_moderator'])

    def test_unauthenticated_user_apiary_details(self):
        response = self.client.get(self.apiary_details_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'apiary/details_apiary.html')

    def test_invalid_pk_apiary_details_authenticated_user(self):

        invalid_apiary_url = reverse('details-apiary', kwargs={'pk': 123})
        response = self.client.get(invalid_apiary_url)
        self.assertEqual(response.status_code, 404)




