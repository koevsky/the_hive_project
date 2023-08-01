from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.validators import UnicodeUsernameValidator

from accounts.models import HiveUser

UserModel = get_user_model()


class HiveUserCreationForm(UserCreationForm):

    username_validator = UnicodeUsernameValidator()

    username = forms.CharField(
        max_length=150,
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your username',
            }
        )
    )

    email = forms.EmailField(
        required=True,
        error_messages={
            "unique": "A user with that e-mail already exists.",
        },
        max_length=150,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your email'
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        required=True,
        max_length=40,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Your password',
            }
        ),
    )

    password2 = forms.CharField(
        label='Repeat password',
        required=True,
        max_length=40,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password confirmation',
            }
        ),
    )

    class Meta:

        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserEditForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'telephone_number', 'profile_picture', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserDeleteForm(UserEditForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True

