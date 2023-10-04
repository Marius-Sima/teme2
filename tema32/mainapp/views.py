from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from mainapp import models
from django.views import View
from mainapp import forms
from django.views.generic import ListView, DetailView, CreateView, FormView
# Create your views here.

class Homepage(ListView):
    model = models.Books
    template_name = "mainapp/home.html"
    context_object_name = "books"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

class BookView(DetailView):
    model = models.Books
    template_name = "mainapp/home.html"
    context_object_name = "books"
    

#class AddBookFormView(FormView):
#    template_name = 'mainapp/add.html'
 #   form_class = forms.BookForm
  #  success_url = '/'
   # def form_valid(self, form):
    #    form.save()


class AddBookFormView(CreateView):
    template_name = "mainapp/add.html"
    form_class = forms.BookForm
    model = models.Books
    success_url = "/"