from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from apiary_app.validators import validate_name_upper, validate_name_symbols

UserModel = get_user_model()


class ApiaryModel(models.Model):

    MIN_NAME_LENGTH = MinLengthValidator(2)

    apiary_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[
            MIN_NAME_LENGTH,
            validate_name_upper,
            validate_name_symbols
        ]
    )

    location = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=[
            MIN_NAME_LENGTH,
            validate_name_upper,
            validate_name_symbols,
        ]
    )

    hives_count = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )

    apiary_photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='apiary_pics'
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.apiary_name} - {self.location}'