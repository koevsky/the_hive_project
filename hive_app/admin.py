from django.contrib import admin
from django.contrib.auth import get_user_model

from apiary_app.models import ApiaryModel
from cart_app.models import CartModel
from hive_app.models import EmailModel
from product_app.models import ProductModel

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(ApiaryModel)
class ApiaryAdmin(admin.ModelAdmin):
    list_display = ['apiary_name', 'location', 'owner']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'apiary', 'owner']


@admin.register(EmailModel)
class MailAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'created_at']


@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']