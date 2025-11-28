from django.urls import path
from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path("", ProdutoListView.as_view(), name="produto_list"),
    path("create/", ProdutoCreateView.as_view(), name="produto_create"),
    path("edit/<int:pk>/", ProdutoUpdateView.as_view(), name="produto_update"),
    path("delete/<int:pk>/", ProdutoDeleteView.as_view(), name="produto_delete")
]
