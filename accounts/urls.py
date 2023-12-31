from django.urls import path, include

from accounts import views

urlpatterns = [

    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([

        path('', views.UserProfilePageView.as_view(), name='profile-page'),
        path('details/', views.UserProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', views.UserEditView.as_view(), name='profile-edit'),
        path('delete/', views.UserDeleteView.as_view(), name='profile-delete'),
        path('apiaries/', views.AllUserApiariesView.as_view(), name='profile-apiaries'),
        path('products/', views.AllUserProductsView.as_view(), name='profile-products'),
        path('orders/', views.AllUserOrdersView.as_view(), name='profile-orders')

    ]))

]