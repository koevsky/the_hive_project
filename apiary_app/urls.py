from django.urls import path

from apiary_app import views

urlpatterns = [
    path('create/', views.ApiaryCreateView.as_view(), name='create-apiary'),
    path('details/<int:pk>/', views.ApiaryDetails.as_view(), name='details-apiary'),
    path('edit/<int:pk>/', views.ApiaryEdit.as_view(), name='edit-apiary'),
    path('delete/<int:pk>/', views.ApiaryDelete.as_view(), name='delete-apiary')
]