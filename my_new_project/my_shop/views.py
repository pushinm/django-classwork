from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Mainpage_view(TemplateView):
    template_name = 'mainpage.html'