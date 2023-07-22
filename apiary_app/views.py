from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from apiary_app.forms import ApiaryForm, ApiaryDeleteForm
from apiary_app.models import ApiaryModel


class ApiaryCreateView(LoginRequiredMixin, CreateView):

    form_class = ApiaryForm
    template_name = 'apiary/create_apiary.html'

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile-apiaries', kwargs={'pk': self.request.user.pk})


class ApiaryDetails(DetailView):

    model = ApiaryModel
    template_name = 'apiary/details_apiary.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['is_user'] = self.request.user == self.object.owner
        context['products_count'] = self.object.productmodel_set.all().count()

        return context


class ApiaryEdit(LoginRequiredMixin, UpdateView):

    form_class = ApiaryForm
    model = ApiaryModel
    template_name = 'apiary/edit_apiary.html'

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)

        if self.request.user != self.object.owner:
            return redirect('index')

        return get

    def get_success_url(self):
        return reverse('details-apiary', kwargs={'pk': self.object.pk})


class ApiaryDelete(LoginRequiredMixin, DeleteView):

    model = ApiaryModel
    template_name = 'apiary/delete_apiary.html'

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)

        if self.request.user != self.object.owner:
            return redirect('index')

        return get

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = ApiaryDeleteForm(instance=self.object)
        return context

    def get_success_url(self):
        return reverse('profile-apiaries', kwargs={'pk': self.request.user.pk})








