from django.urls import path

from product_app import views

urlpatterns = [

    path('create/', views.CreateProductView.as_view(), name='product-create'),
    path('details/<int:pk>/', views.DetailsProductView.as_view(), name='product-details'),
    path('edit/<int:pk>/', views.EditProductView.as_view(), name='product-edit'),
    path('delete/<int:pk>/', views.DeleteProductView.as_view(), name='product-delete'),

]