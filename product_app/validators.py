from django.core.exceptions import ValidationError


def product_name_validator(value: str):
    if not value.isalnum():
        raise ValidationError('Name must consist of letters and numbers!')


