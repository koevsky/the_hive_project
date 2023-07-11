from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from hive_app.forms import ContactForm
from the_hive_project import settings

mail_recipient_list = ['thehiveonlineshop@gmail.com']


class ShowIndexView(TemplateView):
    template_name = 'common/index.html'


class ContactFormView(FormView):

    template_name = 'common/contact_page.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-confirm')

    def form_valid(self, form):

        mail = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_mail(subject, message, mail, mail_recipient_list)
        return super().form_valid(form)


class ShowContactConfirm(TemplateView):
    template_name = 'common/contact_success.html'


class ShowLogoutConfirm(LoginRequiredMixin, TemplateView):
    template_name = 'common/logout_page.html'


class Custom404View(TemplateView):
    template_name = '404.html'

    def get_context_data(self,request, *args, **kwargs):
        self.response = self.render_to_response(self.get_context_data(*args, **kwargs))
        self.response.status_code = 404
        return self.response
