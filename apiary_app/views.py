from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from apiary_app.forms import ApiaryForm, ApiaryDeleteForm
from apiary_app.models import ApiaryModel
from the_hive_core.custom_mixins import CustomPermissionUserMixin


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
        context['products_count'] = self.object.productmodel_set.all().count()
        context['is_user'] = self.request.user == self.object.owner
        context['is_auth'] = self.request.user.is_authenticated
        context['is_admin'] = self.request.user.groups.filter(name='Admin').exists()
        context['is_moderator'] = self.request.user.groups.filter(name='Moderator').exists()

        return context


class ApiaryEdit(CustomPermissionUserMixin, LoginRequiredMixin, UpdateView):

    form_class = ApiaryForm
    model = ApiaryModel
    template_name = 'apiary/edit_apiary.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin', 'Moderator']
        user = self.get_object().owner
        return super().dispatch(request, groups, user, *args, **kwargs)

    def get_success_url(self):
        return reverse('details-apiary', kwargs={'pk': self.object.pk})


class ApiaryDelete(CustomPermissionUserMixin, LoginRequiredMixin, DeleteView):

    model = ApiaryModel
    template_name = 'apiary/delete_apiary.html'

    def dispatch(self, request, *args, **kwargs):
        groups = ['Admin']
        user = self.get_object().owner
        return super().dispatch(request, groups, user, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = ApiaryDeleteForm(instance=self.object)
        return context

    def get_success_url(self):
        return reverse('profile-apiaries', kwargs={'pk': self.request.user.pk})








