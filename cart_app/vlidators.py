from django.core.exceptions import ValidationError


def name_letters_validator(value: str):

    if not value.isalpha():
        return ValidationError('Name must consist of letters only!')


def name_upper_validator(value: str):

    if not value.isupper():
        return ValidationError('Name must start with capital letter!')


