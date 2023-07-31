from unittest import TestCase

from django.core.exceptions import ValidationError

from accounts.validators import telephone_number_validator, INVALID_TELEPHONE_NUMBER_MESSAGE


class TelephoneNumberTest(TestCase):

    def test_valid_number_starts_with_plus(self):

        phone = '+359882123123'
        telephone_number_validator(phone)

    def test_valid_number_strats_with_zero(self):

        phone = '0882123123'
        telephone_number_validator(phone)

    def test_invalid_number_starts_with_plus_too_short(self):

        phone = '+35988212312'

        expected_error_message = INVALID_TELEPHONE_NUMBER_MESSAGE

        with self.assertRaises(ValidationError) as er:
            telephone_number_validator(phone)

        self.assertIsNotNone(er.exception)
        self.assertEqual(er.exception.message, expected_error_message)

    def test_invalid_number_starts_with_plus_not_isdigit(self):

        phone = '+359882123a23'

        expected_error_message = INVALID_TELEPHONE_NUMBER_MESSAGE

        with self.assertRaises(ValidationError) as er:
            telephone_number_validator(phone)

        self.assertIsNotNone(er.exception)
        self.assertEqual(er.exception.message, expected_error_message)

    def test_invalid_number_starts_with_zero_wrong_length(self):

        phone = '08821231234'

        expected_error_message = INVALID_TELEPHONE_NUMBER_MESSAGE

        with self.assertRaises(ValidationError) as er:
            telephone_number_validator(phone)

        self.assertIsNotNone(er.exception)
        self.assertEqual(er.exception.message, expected_error_message)

    def test_test_invalid_number_starts_with_zero_is_not_alpha(self):
        phone = '0882123a23'

        expected_error_message = INVALID_TELEPHONE_NUMBER_MESSAGE

        with self.assertRaises(ValidationError) as er:
            telephone_number_validator(phone)

        self.assertIsNotNone(er.exception)
        self.assertEqual(er.exception.message, expected_error_message)





