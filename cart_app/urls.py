from django.urls import path

from cart_app import views

urlpatterns = [
    path('details/', views.cart_view, name='cart-details'),
    path('add/<int:pk>/', views.add_to_cart, name='cart-add'),
    path('remove/<int:pk>/', views.remove_from_cart, name='cart-remove'),
    path('update/<int:pk>/', views.update_cart, name='cart-update'),
    path('checkout/', views.checkout_page, name='checkout')

]