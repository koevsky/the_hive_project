from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from accounts.models import HiveUser
from apiary_app.models import ApiaryModel
from cart_app.models import Order

from product_app.models import ProductModel
from the_hive_core.custom_mixins import CustomPermissionUserMixin


class ShowCustomAdminPage(CustomPermissionUserMixin, LoginRequiredMixin, TemplateView):

    template_name = 'custom_admin/custom_admin_page.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        user = None
        return super().dispatch(request, groups, user, *args, **kwargs)


class ShowAllUsers(CustomPermissionUserMixin, LoginRequiredMixin, ListView):

    model = HiveUser
    template_name = 'custom_admin/all_users.html'
    context_object_name = 'users'
    ordering = ['-id']

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        user = None
        return super().dispatch(request, groups, user, *args, **kwargs)


class ShowAllApiaries(CustomPermissionUserMixin, LoginRequiredMixin, ListView):

    model = ApiaryModel
    template_name = 'custom_admin/all_apiaries.html'
    context_object_name = 'bee_gardens'
    ordering = ['-id']

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        user = None
        return super().dispatch(request, groups, user, *args, **kwargs)


class ShowAllProducts(CustomPermissionUserMixin, LoginRequiredMixin, ListView):

    model = ProductModel
    template_name = 'custom_admin/all_products.html'
    context_object_name = 'products'
    ordering = ['-id']

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        user = None
        return super().dispatch(request, groups, user, *args, **kwargs)


class ShowAllOrders(CustomPermissionUserMixin, LoginRequiredMixin, ListView):

    model = Order
    template_name = 'custom_admin/all_orders.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        user = None
        return super().dispatch(request, groups, user, *args, **kwargs)

