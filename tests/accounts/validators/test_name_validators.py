from unittest import TestCase

from django.core.exceptions import ValidationError

from accounts.validators import validate_name_is_alpha, validate_name_starts_with_upper


class UserNamesTest(TestCase):

    def test_valid_name_isalpha(self):

        name = 'Testname'
        validate_name_is_alpha(name)

    def test_invalid_name_is_alpha(self):

        name = 'Testname1'
        expected_error_message = 'Name must consist of letters only!'

        with self.assertRaises(ValidationError) as er:
            validate_name_is_alpha(name)

        self.assertIsNotNone(er.exception)
        self.assertEqual(expected_error_message, er.exception.message)

    def test_valid_name_starts_with_capital(self):

        name = 'Testname'
        validate_name_starts_with_upper(name)


    def test_invalid_name_starts_with_lower(self):

        name = 'testname'
        expected_error_message = 'Name must start with capital letter!'

        with self.assertRaises(ValidationError) as er:
            validate_name_starts_with_upper(name)

        self.assertIsNotNone(er.exception)
        self.assertEqual(expected_error_message, er.exception.message)


