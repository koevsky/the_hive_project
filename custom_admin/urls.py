from django.urls import path

from custom_admin import views

urlpatterns = [
    path('', views.ShowCustomAdminPage.as_view(), name='custom-admin'),
    path('all-users/', views.ShowAllUsers.as_view(), name='all-users'),
    path('all-beegardens/', views.ShowAllApiaries.as_view(), name='all-beegardens'),
    path('all-products/', views.ShowAllProducts.as_view(), name='all-products'),
    path('all-orders/', views.ShowAllOrders.as_view(), name='all-orders')
]