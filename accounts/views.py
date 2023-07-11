from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import HiveUserCreationForm, UserLoginForm

UserModel = get_user_model()


class UserRegisterView(CreateView):

    model = UserModel
    form_class = HiveUserCreationForm
    template_name = 'profile/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = 'profile/login.html'
    next_page = reverse_lazy('index')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')


class UserProfilePageView(DetailView):

    model = UserModel
    template_name = 'profile/profile_page.html'





