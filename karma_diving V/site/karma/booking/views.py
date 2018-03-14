from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from booking.forms import ClientForm
from booking.models import Client
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
class CreateClientView(CreateView):
    login_url = '/booking/'
    redirect_field_name = 'index.html'
    form_class = ClientForm
    model = Client

# def add_comment_to_post(request, pk):
#     client = get_object_or_404(Client, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.client = client
#             booking.save()
#             return redirect('index.html')
#     else:
#         form = ClientForm()
#     return render(request, 'index.html', {'form': form})
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
