from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from booking.forms import ClientForm
from booking.models import Client

# Create your views here.
class CreateClientView(CreateView):
    login_url = '/booking/'
    redirect_field_name = 'index.html'
    form_class = ClientForm
    model = Client
