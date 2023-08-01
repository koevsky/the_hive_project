from django.test import TestCase

from accounts.forms import HiveUserCreationForm
from accounts.models import HiveUser


class UserCreationFormTests(TestCase):

    VALID_FORM_DATA = {
        'username': 'testuser',
        'email': 'test@mail.com',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }

    VALID_USER_CREATION_DATA = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword'
    }

    def test_blank_form(self):

        form = HiveUserCreationForm({})
        self.assertFalse(form.is_valid())

    def test_valid_form(self):

        form = HiveUserCreationForm(self.VALID_FORM_DATA)
        self.assertTrue(form.is_valid())

    def test_unique_username(self):

        HiveUser.objects.create_user(
            **self.VALID_USER_CREATION_DATA
        )

        form = HiveUserCreationForm(self.VALID_FORM_DATA)

        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertEqual(form.errors['username'], ['A user with that username already exists.'])

    def test_unique_email(self):

        HiveUser.objects.create_user(
           **self.VALID_USER_CREATION_DATA
        )

        data = {
           **self.VALID_FORM_DATA,
            'user': 'testuser1',
            'email': 'test@example.com'
        }

        form = HiveUserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ['A user with that e-mail already exists.'])

