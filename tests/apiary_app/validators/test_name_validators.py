from django.core.exceptions import ValidationError
from django.test import TestCase

from apiary_app.validators import validate_name_upper, validate_name_symbols, validate_is_whitespace


class ApiaryValidatorsTests(TestCase):

    def test_apiary_name_startswith_lower_raises_validation_error(self):

        name = 'testname'
        expected_message = 'Name must start with uppercase latter!'

        with self.assertRaises(ValidationError) as er:
            validate_name_upper(name)

        self.assertEqual(er.exception.message, expected_message)

    def test_apiary_name_has_prohibited_symbols_raises_validation_error(self):

        name = 'test+'
        expected_message = 'Name must consist of letters, digits or white space!'

        with self.assertRaises(ValidationError) as er:
            validate_name_symbols(name)

        self.assertEqual(er.exception.message, expected_message)

    def test_name_is_white_space_raises_validation_error(self):

        name = '  '
        expected_message = 'Name cannot be whitespace!'

        with self.assertRaises(ValidationError) as er:
            validate_is_whitespace(name)

        self.assertEqual(er.exception.message, expected_message)

