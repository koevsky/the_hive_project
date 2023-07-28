from django.core.exceptions import ValidationError


def name_letters_validator(value: str):

    if not value.isalpha():
        raise ValidationError('Name must consist of letters only!')


def name_upper_validator(value: str):

    if not value[0].isupper():
        raise ValidationError('Name must start with capital letter!')


def zip_code_length(value: int):

    if len(str(value)) < 4:
        raise ValidationError('Zip code must be 4 digits!')


def card_names_validator(value:str):

    if len(value.split()) < 2:
        raise ValidationError('Input first and last name on your card!')


def card_names_start_with_capital(value: str):

    names = value.split()

    for name in names:
        if not name[0].isupper():
            raise ValidationError('Names must start with capital letter!')


def validate_card_digits(value: str):

    if not str(value).isdigit():
        raise ValidationError('Number must consist only of digits!')


def cvv_digits_count(value: int):

    if not len(str(value)) == 3:
        raise ValidationError('CVV must be 3 digits!')


