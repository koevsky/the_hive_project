from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import HiveUser
from apiary_app.models import ApiaryModel
from product_app.models import ProductModel


class ApiaryModelTests(TestCase):

    VALID_USER_CREATION_DATA = {
        'username': 'testusername',
        'email': 'test@mail.com',
        'password': 'testpass123',
    }

    VALID_APIARY_DATA = {
        'apiary_name': 'Testgarden',
        'location': 'Testtown',
        'hives_count': 5,
        'apiary_photo': None,
        'description': None,
        'owner': None
    }

    VALID_PRODUCT_DATA = {

        'product_name': None,
        'product_type': 'Honey',
        'product_image': None,
        'description': None,
        'price': 22,
        'grams': 22,
        'quantity': 22,
        'apiary': None,
        'owner': None
    }

    def test_crate_apiary_with_valid_data(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_CREATION_DATA)
        full_apiary_data = {**self.VALID_APIARY_DATA, 'owner': user}
        apiary = ApiaryModel.objects.create(**full_apiary_data)

        self.assertIsNotNone(apiary.pk)
        self.assertIsInstance(apiary, ApiaryModel)

    def test_crate_apiary_invalid_name(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_CREATION_DATA)
        full_apiary_data = {**self.VALID_APIARY_DATA, 'owner': user, 'apiary_name': '+m'}

        with self.assertRaises(ValidationError) as er:
            apiary = ApiaryModel.objects.create(**full_apiary_data)
            apiary.full_clean()

        self.assertIsNotNone(er.exception)
        self.assertIn('Name must consist of letters, digits or white space!', er.exception.message_dict['apiary_name'])
        self.assertIn('Name must start with uppercase latter!', er.exception.message_dict['apiary_name'])

    def test_apiary_app_invalid_hives_count(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_CREATION_DATA)
        full_apiary_data = {**self.VALID_APIARY_DATA, 'owner': user, 'hives_count': 0}

        with self.assertRaises(ValidationError) as er:
            apiary = ApiaryModel.objects.create(**full_apiary_data)
            apiary.full_clean()

        self.assertIsNotNone(er.exception)
        self.assertIn('Ensure this value is greater than or equal to 1.', er.exception.message_dict['hives_count'])

    def test_apiary_app_string(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_CREATION_DATA)
        full_apiary_data = {**self.VALID_APIARY_DATA, 'owner': user, 'hives_count': 0}
        apiary = ApiaryModel.objects.create(**full_apiary_data)

        self.assertEqual('Testgarden - Testtown', str(apiary))

    def test_products_count_from_apiary(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_CREATION_DATA)
        full_apiary_data = {**self.VALID_APIARY_DATA, 'owner': user}
        apiary = ApiaryModel.objects.create(**full_apiary_data)
        product_data = {**self.VALID_PRODUCT_DATA, 'apiary': apiary, 'owner': user, 'product_name': ''}
        products_count = 3

        for x in range(products_count):
            product_data['product_name'] = f'Product{x}'
            ProductModel.objects.create(**product_data)

        self.assertEqual(apiary._owner_products(), products_count)























