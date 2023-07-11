from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.validators import UnicodeUsernameValidator


UserModel = get_user_model()


class HiveUserCreationForm(UserCreationForm):

    username_validator = UnicodeUsernameValidator()

    username = forms.CharField(
        max_length=150,
        help_text='',
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your username',
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Your password',
                'class': 'form-control'
            }
        ),
    )

    password2 = forms.CharField(
        label='Repeat password',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password confirmation',
                'class': 'form-control'
            }
        ),
    )

    class Meta:

        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'class': 'form-control'
                }
            ),
        }


class UserLoginForm(AuthenticationForm):

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username',
                'class': 'form-control'

            }
        )
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )




