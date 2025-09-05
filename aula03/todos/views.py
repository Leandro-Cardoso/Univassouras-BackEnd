from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"  # Local do template
    context_object_name = "todos"           # Nome da lista no template
