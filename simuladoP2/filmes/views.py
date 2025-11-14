from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Filme

class FilmeListView(View):
    template_name = 'filmes/filme_list.html'

    def get(self, request):
        filmes = Filme.objects.all()
        context = {'filmes': filmes}
        return render(request, self.template_name, context)

class FilmeCreateView(CreateView):
    model = Filme
    fields = ["titulo", "diretor", "nota"]
    success_url = reverse_lazy("filme_list")

class FilmeUpdateView(UpdateView):
    model = Filme
    fields = ["titulo", "diretor", "nota"]
    success_url = reverse_lazy("filme_list")

class FilmeDeleteView(DeleteView):
    model = Filme
    success_url = reverse_lazy("filme_list")
