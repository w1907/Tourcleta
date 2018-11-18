from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mantenedor.models import Book
#from catalogo.models import Bicicleta

# Create your views here.
"""
class BookList(ListView):
    model = Bicicleta

class BookCreate(CreateView):
    model = Bicicleta
    fields = ['marca', 'aro','precio','imagen_bicicleta']
    success_url = reverse_lazy('mantenedor:book_list')

class BookUpdate(UpdateView):
    model = Bicicleta
    fields = ['marca', 'aro','precio','imagen_bicicleta']
    success_url = reverse_lazy('catalogo:book_list')

class BookDelete(DeleteView):
    model = Bicicleta
    success_url = reverse_lazy('catalogo:book_list')
"""
class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('mantenedor:book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('mantenedor:book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('mantenedor:book_list')

