from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

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
        context['is_user'] = self.request.user == self.object.owner

        return context


class EditProductView(LoginRequiredMixin, UpdateView):

    model = ProductModel
    form_class = ProductForm
    template_name = 'product/edit_product.html'

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)

        if self.request.user != self.object.owner:
            return redirect('index')

        return get

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.object.pk})


class DeleteProductView(LoginRequiredMixin, DeleteView):

    model = ProductModel
    template_name = 'product/delete_product.html'

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)

        if self.request.user != self.object.owner:
            return redirect('index')

        return get

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteProductForm(instance=self.object, user=self.object.owner)
        return context

    def get_success_url(self):
        return reverse('profile-products', kwargs={'pk': self.request.user.pk})
