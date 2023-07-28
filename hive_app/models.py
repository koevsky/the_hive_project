from django.contrib.auth import get_user_model
from django.db import models

from product_app.models import ProductModel


UserModel = get_user_model()


class Like(models.Model):

    to_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )


