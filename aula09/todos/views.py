from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy

from .models import Todo, Category

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = Todo
    fields = [
        'title',
        'description',
        'category'
    ]
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = [
        'title',
        'description',
        'category',
        'is_completed'
    ]
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')

class TodoCompletarView(View):
    """
    Classe que marca uma tarefa como concluída.
    """

    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.is_completed = True
        todo.save()

        return redirect("todo_list")
