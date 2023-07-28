from django.contrib import admin
from django.contrib.auth import get_user_model

from apiary_app.models import ApiaryModel
from cart_app.models import Cart, Order, CartItem
from hive_app.models import Like
from product_app.models import ProductModel

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'email']
    ordering = ['pk', '-last_login', ]

    readonly_fields = ['password', 'username', 'email', 'first_name', 'last_name', 'last_login', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['username', 'email', 'first_name', 'last_name']

    fieldsets = [
        ['Credentials:', {'fields': ['username', 'email', 'password']}],
        ['Login data:', {'fields': ['last_login', 'date_joined']}],
        ['Optional data:', {'fields': ['first_name', 'last_name', 'telephone_number', 'description', 'profile_picture']}],
        ['Permissions and status:', {'fields': ['is_staff', 'is_superuser', 'groups', 'user_permissions']}]
    ]

    list_per_page = 10


@admin.register(ApiaryModel)
class ApiaryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'apiary_name', 'location', 'owner']
    ordering = ['owner', 'pk']

    readonly_fields = ['hives_count', 'owner']
    search_fields = ['apiary_name', 'location', 'owner']
    list_filter = ['hives_count', 'owner']

    fieldsets = [
        ['Basic apiary information:', {'fields': ['apiary_name', 'location', 'hives_count', 'apiary_photo']}],
        ['Owner information:', {'fields': ['owner']}]
    ]

    list_per_page = 10


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk','product_name', 'apiary', 'owner']
    ordering = ['pk']

    readonly_fields = ['owner', 'apiary', 'quantity', 'grams']
    search_fields = ['product_name', 'description']
    list_filter = ['product_name', 'apiary']

    fieldsets = [
        ['Basic product information:', {'fields': ['product_name', 'product_type', 'product_image', 'description']}],
        ['Storage information:', {'fields': ['grams', 'price', 'quantity']}],
        ['Related to:', {'fields': ['owner', 'apiary']}]
    ]

    list_per_page = 10


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user']
    ordering = ['pk', 'user']

    readonly_fields = ['items']
    search_fields = ['user']
    list_filter = ['user']

    fieldsets = [
        ['Cart user:', {'fields': ['user']}],
        ['Cart items:', {'fields': ['items']}]
    ]

    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'created_at', 'user', 'all_items_count', 'total_order_price']
    ordering = ['created_at']

    readonly_fields = [
        'card_number', 'cvv', 'user', 'items',
        'total_order_price', 'all_items_count',
        'expiration_date', 'name_on_card', 'created_at'
    ]
    search_fields = ['first_name', 'last_name', 'user', 'all_items_count']
    list_filter = ['created_at', 'user', 'first_name', 'last_name']

    fieldsets = [
        ['User credentials:', {'fields': ['user', 'first_name', 'last_name', 'address', 'country', 'city', 'zip_code']}],
        ['Basic order information:', {'fields': ['items', 'total_order_price', 'all_items_count', 'created_at']}]

    ]

    list_per_page = 10


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    ordering = ['id', 'product']

    readonly_fields = ['product']
    search_fields = ['product']
    list_filter = ['product']

    fieldsets = [
        ['Basic cart item information', {'fields': ['product', 'quantity']}]
    ]

    list_per_page = 10


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'to_product', 'user']
    ordering = ['id']

    readonly_fields = ['to_product', 'user']
    search_fields = ['to_product', 'user']
    list_filter = ['to_product', 'user']

    fieldsets = [
        ['Liked product:', {'fields': ['to_product']}],
        ['By user:', {'fields': ['user']}]
    ]

    list_per_page = 10

