from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.templatetags.static import static
from apiary_app.models import ApiaryModel
from product_app.validators import product_name_validator

UserModel = get_user_model()


class ProductModel(models.Model):

    MIN_NAME_LENGTH = MinLengthValidator(3)
    MIN_PRICE_VALIDATOR = MinValueValidator(1)
    MIN_QTY_VALIDATOR = MinValueValidator(1)
    MIN_GRAMS_VALIDATOR = MinValueValidator(1)

    HONEY = 'Honey'
    POLLEN = 'Pollen'
    PROPOLIS = 'Propolis'

    PRODUCT_TYPES = [
        (HONEY, HONEY),
        (POLLEN, POLLEN),
        (PROPOLIS, PROPOLIS)
    ]

    product_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[
            product_name_validator,
            MIN_NAME_LENGTH,
        ]
    )

    product_type = models.CharField(
        blank=False,
        null=False,
        choices=PRODUCT_TYPES
    )

    product_image = models.ImageField(
        blank=True,
        null=True,
        upload_to='product_pics',
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MIN_PRICE_VALIDATOR
        ],
        max_length=30
    )

    grams = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MIN_GRAMS_VALIDATOR
        ]
    )

    quantity = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            MIN_QTY_VALIDATOR
        ]
    )

    apiary = models.ForeignKey(
        ApiaryModel,
        on_delete=models.CASCADE
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

