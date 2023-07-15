from django.contrib.auth import get_user_model
from django.db import models

from product_app.models import ProductModel


UserModel = get_user_model()


class CartModel(models.Model):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)


