from django.core.exceptions import ValidationError


def product_name_validator(value: str):

    for char in value:

        if not (char == " " or char.isalnum()):
            raise ValidationError('Name must consist of letters and numbers!')


