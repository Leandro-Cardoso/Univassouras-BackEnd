from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Livro

class LivroListView(ListView):
    model = Livro
    template_name = "biblioteca/livro_list.html"
    context_object_name = "livros"

class LivroCreateView(CreateView):
    model = Livro
    fields = ["titulo", "ano_publicacao", "autor"]
    success_url = reverse_lazy("livro_list")

class LivroUpdateView(UpdateView):
    model = Livro
    fields = ["titulo", "ano_publicacao", "autor"]
    success_url = reverse_lazy("livro_list")

class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy("livro_list")
