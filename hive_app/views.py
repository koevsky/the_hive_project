from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView
from hive_app.forms import ContactForm
from hive_app.models import Like
from product_app.models import ProductModel
from django.core.mail import send_mail

from the_hive_project import settings


class ShowIndexView(TemplateView):

    template_name = 'common/index.html'


class ContactFormCreate(FormView):

    form_class = ContactForm
    template_name = 'common/contact_page.html'
    success_url = reverse_lazy('contact-confirm')

    def form_valid(self, form):

        mail = form.cleaned_data['your_email']

        subject = form.cleaned_data['subject']
        subject = f"From: {mail} -> Subject: {subject}"

        message = form.cleaned_data['message']
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, recipient_list)

        return super().form_valid(form)


class MailSentView(TemplateView):
    template_name = 'common/contact_success.html'


class ShowLogoutConfirm(LoginRequiredMixin, TemplateView):
    template_name = 'common/logout_page.html'


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
        context['is_auth'] = self.request.user.is_authenticated
        context['Search'] = self.request.GET.get('Search', '')

        return context


class ShowProductOnly(ListView):

    model = ProductModel
    template_name = 'common/product_type_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_name'] = self.kwargs.get('product_type')

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        product_type = self.kwargs.get('product_type')
        queryset = queryset.filter(product_type=product_type)
        return queryset


@login_required(login_url='login')
def like_functionality(request, pk):

    product = ProductModel.objects.get(pk=pk)

    kwargs = {
        'to_product': product,
        'user': request.user
    }

    like = Like.objects.filter(**kwargs).first()

    if like:
        like.delete()

    else:
        like = Like(**kwargs)
        like.save()

    url = request.META['HTTP_REFERER']
    return redirect(url)
