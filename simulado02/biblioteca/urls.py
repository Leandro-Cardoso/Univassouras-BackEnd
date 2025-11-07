from django.urls import path
from biblioteca.views import LivroListView, LivroCreateView, LivroUpdateView, LivroDeleteView

urlpatterns = [
    path("", LivroListView.as_view(), name="livro_list"),
    path("create/", LivroCreateView.as_view(), name="livro_create"),
    path("edit/<int:pk>/", LivroUpdateView.as_view(), name="livro_update"),
    path("delete/<int:pk>/", LivroDeleteView.as_view(), name="livro_delete"),
]
