from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models

from cart_app.vlidators import name_upper_validator, name_letters_validator, zip_code_length, card_names_validator, \
    card_names_start_with_capital, validate_card_digits, cvv_digits_count

from product_app.models import ProductModel


UserModel = get_user_model()


class CartItem(models.Model):

    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=1,
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f'{self.product.product_name} - {self.quantity}'

    def item_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    items = models.ManyToManyField(
        CartItem,
        blank=True
    )

    def total_price(self):
        return sum(item.item_price() for item in self.items.all())


class Order(models.Model):

    MIN_LENGTH = MinLengthValidator(2)

    DEBIT = 'Debit card'
    CREDIT = 'Credit card'

    PAYMENT_CHOICES = [
        (DEBIT, DEBIT),
        (CREDIT, CREDIT)
    ]

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        validators=[
            name_upper_validator,
            name_letters_validator,
            MIN_LENGTH
        ]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        validators=[
            name_upper_validator,
            name_letters_validator,
            MIN_LENGTH
        ]
    )

    address = models.CharField(
        blank=False,
        null=False,
        max_length=150,
        validators=[
            MIN_LENGTH,
        ]
    )

    country = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        validators=[
            name_letters_validator,
            name_upper_validator,
            MIN_LENGTH
        ]
    )

    city = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        validators=[
            name_upper_validator,
            name_letters_validator,
            MIN_LENGTH
        ]
    )

    zip_code = models.CharField(
        blank=False,
        null=False,
        validators=[
            zip_code_length
        ]
    )

    payment_method = models.CharField(
        blank=False,
        null=False,
        choices=PAYMENT_CHOICES
    )

    name_on_card = models.CharField(
        blank=False,
        null=False,
        max_length=100,
        validators=[
            card_names_validator,
            card_names_start_with_capital
        ],
    )

    card_number = models.CharField(
        blank=False,
        null=False,
        validators=[
            validate_card_digits,
            MinLengthValidator(10),
            MaxLengthValidator(19)
        ]

    )

    expiration_date = models.DateField(
        blank=False,
        null=False,
        auto_now_add=False,
        verbose_name= 'Expiration date [dd/mm/yy]'

    )

    cvv = models.CharField(
        blank=False,
        null=False,
        validators=[
            validate_card_digits,
            cvv_digits_count
        ]
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    items = models.ManyToManyField(
        CartItem,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order №{self.pk} - By: {self.user}'

    def all_items_count(self):
        return sum(item.quantity for item in self.items.all())

    def total_order_price(self):
        return sum(item.item_price() for item in self.items.all())