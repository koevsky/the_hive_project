from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', include([
        path('', views.UserProfilePageView.as_view(), name='profile-page'),
    ]))
]