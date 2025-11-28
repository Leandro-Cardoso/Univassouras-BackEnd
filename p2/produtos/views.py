from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/produto_list.html"
    context_object_name = "produtos"

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ["name", "category", "price"]
    success_url = reverse_lazy("produto_list")

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ["name", "category", "price"]
    success_url = reverse_lazy("produto_list")

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy("produto_list")
