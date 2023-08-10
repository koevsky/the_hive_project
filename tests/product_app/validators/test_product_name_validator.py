from django.core.exceptions import ValidationError
from django.test import TestCase

from product_app.validators import product_name_validator


class ProductModelValidatorsTests(TestCase):

    def test_product_name_invalid_chars(self):

        wrong_name = '+testname'

        with self.assertRaises(ValidationError) as er:
            product_name_validator(wrong_name)

        self.assertEqual(er.exception.message, 'Name must consist of letters and numbers!')

    def test_product_name_valid_with_space(self):

        valid_name = 'Test Name'

        message = product_name_validator(valid_name)

        self.assertIsNone(message)
