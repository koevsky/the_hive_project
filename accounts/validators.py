from django.core.exceptions import ValidationError


INVALID_TELEPHONE_NUMBER_MESSAGE = 'Invalid number!'


def validate_name_is_alpha(value: str):

    if not value.isalpha():
        raise ValidationError('Name must consist of letters only!')


def validate_name_starts_with_upper(value: str):

    if not value[0].isupper():
        raise ValidationError('Name must start with capital letter!')


def telephone_number_validator(value: str):

    if value[0] == '+':

        if not (value[1:].isdigit() and len(value) == 13):
            raise ValidationError(INVALID_TELEPHONE_NUMBER_MESSAGE)

    elif value.isdigit():

        if len(value) != 10:
            raise ValidationError(INVALID_TELEPHONE_NUMBER_MESSAGE)

    else:
        raise ValidationError(INVALID_TELEPHONE_NUMBER_MESSAGE)




