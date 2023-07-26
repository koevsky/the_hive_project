from django.urls import path

from cart_app import views

urlpatterns = [

    path('details/', views.cart_view, name='cart-details'),
    path('add/<int:pk>/', views.add_to_cart, name='cart-add'),
    path('remove/<int:pk>/', views.remove_from_cart, name='cart-remove'),
    path('update/<int:pk>/', views.update_cart, name='cart-update'),

    path('checkout/', views.checkout_page, name='checkout'),

    path('order-success/', views.successful_order_page, name='order-success'),
    path('order-delete/<int:pk>/', views.delete_order, name='order-delete'),
    path('order-details/<int:pk>/', views.order_details, name='order-details'),
    path('delete-item/<int:pk>/', views.delete_item, name='item-delete'),
    path('edit-item/<int:pk>/', views.edit_item, name='item-edit')

]