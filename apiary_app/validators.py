from django.core.exceptions import ValidationError


def validate_name_upper(value: str):
    if not value[0].isupper():
        raise ValidationError('Name must start with uppercase latter!')


def validate_name_symbols(value: str):

    prohibited_symbols = ['+', '_', '-', '!', '@', '^']

    if set(value).intersection(prohibited_symbols):
        raise ValidationError('Name must consist of letters, digits or white space!')


def validate_is_whitespace(value: str):

    if value.isspace():
        raise ValidationError('Name cannot be whitespace!')


