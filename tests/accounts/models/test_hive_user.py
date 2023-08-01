from django.core.exceptions import ValidationError
from django.db import DataError
from django.test import TestCase

from accounts.models import HiveUser


class HiveUserTests(TestCase):

    VALID_USER_DATA = {
        'username': 'testuser',
        'email': 'test@mail.com',
        'password': 'testpass123'
    }

    VALID_USER_DATA_FULL = {
        'username': 'testuser',
        'email': 'test@mail.com',
        'password': 'testpass123',
        'first_name': 'Testfirst',
        'last_name': 'Testlast',
        'telephone_number': '1234567890',
        'description': 'Test user description'
    }

    def test_create_user_with_register_data(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_DATA)

        self.assertIsNotNone(user.pk)
        self.assertIsInstance(user, HiveUser)
        self.assertTrue(user.check_password('testpass123'))

    def test_create_valid_superuser(self):
        superuser = HiveUser.objects.create_superuser(**self.VALID_USER_DATA)

        self.assertIsInstance(superuser, HiveUser)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_valid_user_full_data(self):
        user = HiveUser.objects.create_user(**self.VALID_USER_DATA_FULL)

        self.assertIsNotNone(user.pk)
        self.assertIsInstance(user, HiveUser)
        self.assertTrue(user.check_password('testpass123'))
        self.assertEqual(user.get_full_name(), 'Testfirst Testlast')
        self.assertEqual(user.telephone_number, '1234567890')
        self.assertEqual(user.description, 'Test user description')

    def test_invalid_first_name_has_one_more_characters(self):

        invalid_data = {**self.VALID_USER_DATA_FULL, 'first_name': 'X' + HiveUser.DEFAULT_MAX_LENGTH * 'x'}

        with self.assertRaises(DataError):
            user = HiveUser.objects.create_user(
                **invalid_data,
            )
            user.clean_fields()

    def test_invalid_last_name_has_one_more_characters(self):

        invalid_data = {**self.VALID_USER_DATA_FULL, 'last_name': 'X' + HiveUser.DEFAULT_MAX_LENGTH * 'x'}

        with self.assertRaises(DataError):
            user = HiveUser.objects.create_user(
                **invalid_data,
            )
            user.clean_fields()

    def test_wrong_user_telephone_raise_validation_error(self):
        invalid_data = {**self.VALID_USER_DATA_FULL, 'telephone_number': 'test123994556'}

        with self.assertRaises(ValidationError) as er:
            user = HiveUser.objects.create_user(
                **invalid_data,
            )
            user.clean_fields()

        self.assertIsNotNone(er.exception)














