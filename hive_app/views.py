from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from hive_app.forms import ContactForm

mail_recipient_list = ['kaloyankoev9601@gmail.com', 'thehiveonlineshop@gmail.com']


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
