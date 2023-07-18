from django.urls import path

from hive_app import views

urlpatterns = [

    path('', views.ShowIndexView.as_view(), name='index'),
    path('contacts/', views.ContactFormCreate.as_view(), name='contact'),
    path('contacts/confirm/', views.MailSentView.as_view(), name='contact-confirm'),
    path('logout/confirm/', views.ShowLogoutConfirm.as_view(), name='logout-confirm'),
    path('shop/', views.ShopPageView.as_view(), name='shop')

]
