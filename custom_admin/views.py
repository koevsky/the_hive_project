from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from accounts.models import HiveUser
from apiary_app.models import ApiaryModel
from cart_app.models import Order, CartItem, Cart
from hive_app.models import Like
from product_app.models import ProductModel
from the_hive_core.custom_mixins import CustomPermissionAdminMixin


class ShowCustomAdminPage(CustomPermissionAdminMixin, LoginRequiredMixin, TemplateView):

    template_name = 'custom_admin/custom_admin_page.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        return super().dispatch(request, groups, *args, **kwargs)


class ShowAllUsers(CustomPermissionAdminMixin, LoginRequiredMixin, ListView):

    model = HiveUser
    template_name = 'custom_admin/all_users.html'
    context_object_name = 'users'
    ordering = ['-id']

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        return super().dispatch(request, groups, *args, **kwargs)


class ShowAllApiaries(CustomPermissionAdminMixin, LoginRequiredMixin, ListView):

    model = ApiaryModel
    template_name = 'custom_admin/all_apiaries.html'
    context_object_name = 'bee_gardens'
    ordering = ['-id']

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        return super().dispatch(request, groups, *args, **kwargs)


class ShowAllProducts(CustomPermissionAdminMixin, LoginRequiredMixin, ListView):

    model = ProductModel
    template_name = 'custom_admin/all_products.html'
    context_object_name = 'products'
    ordering = ['-id']

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        return super().dispatch(request, groups, *args, **kwargs)


class ShowAllOrders(CustomPermissionAdminMixin, LoginRequiredMixin, ListView):

    model = Order
    template_name = 'custom_admin/all_orders.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        return super().dispatch(request, groups, *args, **kwargs)









