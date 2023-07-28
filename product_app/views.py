from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from the_hive_core.custom_mixins import CustomPermissionUserMixin
from product_app.forms import ProductForm, DeleteProductForm
from product_app.models import ProductModel


class CreateProductView(LoginRequiredMixin, CreateView):

    form_class = ProductForm
    template_name = 'product/create_product.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile-products', kwargs={'pk': self.request.user.pk})


class DetailsProductView(DetailView):

    model = ProductModel
    template_name = 'product/details_product.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['likes'] = self.object.like_set.all().count()
        context['is_auth'] = self.request.user.is_authenticated
        context['is_user'] = self.request.user == self.object.owner
        context['is_admin'] = self.request.user.groups.filter(name='Admin').exists()
        context['is_moderator'] = self.request.user.groups.filter(name='Moderator').exists()

        return context


class EditProductView(CustomPermissionUserMixin, LoginRequiredMixin, UpdateView):

    model = ProductModel
    form_class = ProductForm
    template_name = 'product/edit_product.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin', 'Moderator']
        user = self.get_object().owner
        return super().dispatch(request, groups, user, *args, **kwargs)

    def get_form_kwargs(self):
        self.get_object()
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.object.owner
        return kwargs

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.object.pk})


class DeleteProductView(CustomPermissionUserMixin, LoginRequiredMixin, DeleteView):

    model = ProductModel
    template_name = 'product/delete_product.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        user = self.get_object().owner
        return super().dispatch(request, groups, user, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteProductForm(instance=self.object, user=self.object.owner)
        return context

    def get_success_url(self):
        return reverse('profile-products', kwargs={'pk': self.request.user.pk})
