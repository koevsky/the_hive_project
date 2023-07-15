from django.db import models

from product_app.models import ProductModel


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

