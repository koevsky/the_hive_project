from django.core.exceptions import ValidationError


def names_validator(value: str):

    if not value.isalpha():
        raise ValidationError('Name must consist of letters only!')

    elif not value[0].isupper():
        raise ValidationError('Name must start with capital letter!')


def telephone_number_validator(value: str):

    error_message = 'Invalid number!'

    # + 359 882 398 181

    if value.startswith('+'):

        if not (value[1:].isdigit() and len(value) == 13):
            return ValidationError(error_message)

    elif value.isdigit():

        if len(value) != 10:
            raise ValidationError(error_message)

    else:
        raise ValidationError(error_message)




