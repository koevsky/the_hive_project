from django.shortcuts import render
from django.views.generic import TemplateView


class ShowIndexView(TemplateView):
    template_name = 'common/index.html'

