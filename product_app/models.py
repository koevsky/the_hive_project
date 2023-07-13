from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from apiary_app.models import ApiaryModel

UserModel = get_user_model()


class ProductModel(models.Model):

    min_price_validator = MinValueValidator(1)
    min_qty_validator = MinValueValidator(1)

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
        validators=[]
    )

    product_type = models.CharField(
        blank=False,
        null=False,
        choices=PRODUCT_TYPES
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            min_price_validator
        ]
    )

    quantity = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            min_qty_validator
        ]
    )

    apiary = models.ManyToManyField(
        ApiaryModel,
        blank=False,
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )