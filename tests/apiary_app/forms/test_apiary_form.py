from django.test import TestCase

from accounts.models import HiveUser
from apiary_app.forms import ApiaryForm
from apiary_app.models import ApiaryModel


class ApiaryFormTests(TestCase):

    VALID_FORM_DATA = {

        'apiary_name': 'Testname',
        'location': 'Testtown',
        'hives_count': 5,
        'apiary_photo': None,
        'description': 'Testdescription'

    }

    VALID_USER_DATA = {
        'username': 'testname',
        'email': 'test@mail.com',
        'password': 'testpass123'
    }

    def test_blank_form(self):

        form = ApiaryForm({})
        self.assertFalse(form.is_valid())

    def test_valid_form(self):

        form = ApiaryForm(self.VALID_FORM_DATA)
        self.assertTrue(form.is_valid())

    def test_unique_apiary_name(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_DATA)
        full_apiary_data = {**self.VALID_FORM_DATA, 'owner': user}
        ApiaryModel.objects.create(**full_apiary_data)
        form = ApiaryForm(self.VALID_FORM_DATA)

        self.assertFalse(form.is_valid())
        self.assertIn('apiary_name', form.errors)
        self.assertEqual(form.errors['apiary_name'], ['Apiary model with this Apiary name already exists.'])

    def test_zero_hives_count(self):

        full_apiary_data = {**self.VALID_FORM_DATA, 'hives_count': 0}
        form = ApiaryForm(full_apiary_data)

        self.assertFalse(form.is_valid())
        self.assertIn('hives_count', form.errors)
        self.assertEqual(form.errors['hives_count'], ['Ensure this value is greater than or equal to 1.'])


