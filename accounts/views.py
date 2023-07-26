from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accounts.forms import HiveUserCreationForm, UserLoginForm, UserEditForm, UserDeleteForm
from cart_app.models import Cart

from the_hive_core.custom_mixins import CustomPermissionUserMixin

UserModel = get_user_model()


class UserRegisterView(CreateView):

    model = UserModel
    form_class = HiveUserCreationForm
    template_name = 'profile/register.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)

        if self.request.user.is_authenticated:
            return redirect('index')

        return get

    def form_valid(self, form):

        valid = super().form_valid(form)
        Cart.objects.create(user=self.object)
        login(self.request, self.object)

        return valid


class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = 'profile/login.html'
    next_page = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)

        if self.request.user.is_authenticated:
            return redirect('index')

        return get


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')


class UserProfilePageView(CustomPermissionUserMixin, LoginRequiredMixin, DetailView):

    model = UserModel
    template_name = 'profile/profile_page.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin', 'Moderator']
        user = self.get_object()
        return super().dispatch(request, groups, user, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['is_user'] = self.request.user == self.object
        context['is_admin'] = self.request.user.groups.filter(name='Admin').exists()
        context['is_moderator'] = self.request.user.groups.filter(name='Moderator').exists()

        return context


class UserProfileDetailsView(LoginRequiredMixin, DetailView):

    model = UserModel
    template_name = 'profile/details_profile.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['products'] = self.object.productmodel_set.all()
        context['is_user'] = self.request.user == self.object
        context['is_auth'] = self.request.user.is_authenticated
        context['is_admin'] = self.request.user.groups.filter(name='Admin').exists()
        context['is_moderator'] = self.request.user.groups.filter(name='Moderator').exists()

        return context


class UserEditView(CustomPermissionUserMixin, LoginRequiredMixin, UpdateView):

    model = UserModel
    form_class = UserEditForm
    template_name = 'profile/edit_profile.html'

    def dispatch(self, request, *args, **kwargs):

        groups = ['Admin', 'Moderator']
        user = self.get_object()
        return super().dispatch(request, groups, user, *args, **kwargs)

    def get_success_url(self):

        return reverse('profile-details', kwargs={'pk': self.object.pk})


class UserDeleteView(CustomPermissionUserMixin, LoginRequiredMixin, DeleteView):

    model = UserModel
    template_name = 'profile/delete_profile.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        user = self.get_object()
        return super().dispatch(request, groups, user, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = UserDeleteForm(instance=self.object)

        return context

    def post(self, request, *args, **kwargs):
        self.object.delete()
        return redirect('index')


class AllUserApiariesView(DetailView):

    model = UserModel
    template_name = 'profile/profile_apiaries.html'

    def get_context_data(self, **kwargs):

        addressing = 'Your'

        if self.request.user != self.object:
            addressing = f"{self.object.username}'s"

        context = super().get_context_data(**kwargs)
        context['apiaries'] = self.object.apiarymodel_set.all()
        context['addressing'] = addressing
        context['is_user'] = self.object == self.request.user
        context['is_admin'] = self.request.user.groups.filter(name='Admin').exists()
        context['is_moderator'] = self.request.user.groups.filter(name='Moderator').exists()

        return context


class AllUserProductsView(DetailView):

    model = UserModel
    template_name = 'profile/profile_products.html'

    def get_context_data(self, **kwargs):

        addressing = 'Your'

        if self.request.user != self.object:
            addressing = f"{self.object.username}'s"

        context = super().get_context_data(**kwargs)
        context['products'] = self.object.productmodel_set.all()
        context['addressing'] = addressing
        context['is_user'] = self.object == self.request.user

        return context


class AllUserOrdersView(CustomPermissionUserMixin, LoginRequiredMixin, DetailView):

    model = UserModel
    template_name = 'profile/profile_orders.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin', 'Moderator']
        user = self.get_object()
        return super().dispatch(request, groups, user, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['orders'] = self.object.order_set.all()
        context['is_user'] = self.object == self.request.user
        context['is_admin'] = self.request.user.groups.filter(name='Admin').exists()
        context['is_moderator'] = self.request.user.groups.filter(name='Moderator').exists()

        return context




