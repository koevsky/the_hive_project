from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from hive_app.forms import ContactForm
from hive_app.models import EmailModel
from product_app.models import ProductModel


class ShowIndexView(TemplateView):

    template_name = 'common/index.html'


class ContactFormCreate(CreateView):

    model = EmailModel
    form_class = ContactForm
    template_name = 'common/contact_page.html'
    success_url = reverse_lazy('contact-confirm')


class MailSentView(TemplateView):
    template_name = 'common/contact_success.html'


class ShowLogoutConfirm(LoginRequiredMixin, TemplateView):
    template_name = 'common/logout_page.html'


class Custom404View(TemplateView):
    template_name = '404.html'

    def get_context_data(self,request, *args, **kwargs):
        self.response = self.render_to_response(self.get_context_data(*args, **kwargs))
        self.response.status_code = 404
        return self.response


class ShopPageView(ListView):

    model = ProductModel
    template_name = 'common/shop.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('Search', '')
        queryset = queryset.filter(product_name__icontains=search)
        queryset = queryset.order_by('product_name')

        return queryset

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context['Search'] = self.request.GET.get('Search', '')

        return context



