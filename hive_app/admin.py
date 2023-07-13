from django.contrib import admin
from django.contrib.auth import get_user_model

from apiary_app.models import ApiaryModel

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(ApiaryModel)
class ApiaryAdmin(admin.ModelAdmin):
    list_display = ['apiary_name', 'location', 'owner']