from django.contrib.auth import get_user_model
from django.db import models

from product_app.models import ProductModel


UserModel = get_user_model()


class EmailModel(models.Model):

    email = models.EmailField(
        blank=False,
        null=False,

    )

    subject = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )

    message = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email ID: {self.pk}"


class Like(models.Model):

    to_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )


