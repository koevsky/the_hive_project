from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from cart_app.vlidators import name_upper_validator, name_letters_validator
from product_app.models import ProductModel


UserModel = get_user_model()


class CartModel(models.Model):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ]

    )

    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.product.price


class OrderModel(models.Model):

    MIN_NAME_LENGTH = MinLengthValidator(2)

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[
            name_upper_validator,
            name_letters_validator,
            MIN_NAME_LENGTH
        ]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[
            name_upper_validator,
            name_letters_validator,
            MIN_NAME_LENGTH
        ]
    )





