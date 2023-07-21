from django.contrib import admin
from django.contrib.auth import get_user_model

from apiary_app.models import ApiaryModel
from cart_app.models import Cart, Order, CartItem
from hive_app.models import EmailModel, Like
from product_app.models import ProductModel

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    ordering = ['-last_login']

    readonly_fields = ['password', 'username', 'email', 'first_name', 'last_name', 'last_login', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['username', 'email', 'first_name', 'last_name']

    list_per_page = 10


@admin.register(ApiaryModel)
class ApiaryAdmin(admin.ModelAdmin):
    list_display = ['apiary_name', 'location', 'owner']
    ordering = ['owner']

    readonly_fields = ['hives_count', 'owner']
    search_fields = ['apiary_name', 'location', 'owner']
    list_filter = ['hives_count', 'owner']

    list_per_page = 10


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'apiary', 'owner']
    ordering = ['owner']

    readonly_fields = ['owner', 'quantity', 'grams']
    search_fields = ['product_name', 'description']
    list_filter = ['product_name', 'apiary']

    list_per_page = 10


@admin.register(EmailModel)
class MailAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'created_at']
    ordering = ['created_at']
    readonly_fields = ['email', 'created_at', 'subject']

    list_per_page = 10


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
    ordering = ['user']

    readonly_fields = ['items']
    search_fields = ['user']

    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    ordering = ['created_at']

    readonly_fields = [
        'card_number', 'cvv', 'user',
        'items', 'total_price', 'total_products_qty',
        'expiration_date', 'name_on_card'
    ]
    search_fields = ['first_name', 'last_name', 'user', 'total_price']

    list_per_page = 10


@admin.register(CartItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    ordering = ['product']

    readonly_fields = ['product']
    search_fields = ['product']

    list_per_page = 10


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'to_product', 'user']
    ordering = ['id']

    readonly_fields = ['to_product', 'user']
    search_fields = ['to_product', 'user']

    list_per_page = 10

