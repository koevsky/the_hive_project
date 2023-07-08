from django.urls import path

from hive_app import views

urlpatterns = [
    path('', views.ShowIndexView.as_view(), name='index')
]
