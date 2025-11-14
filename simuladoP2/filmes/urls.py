from django.urls import path
from filmes.views import (
    FilmeListView,
    FilmeCreateView,
    FilmeUpdateView,
    FilmeDeleteView
)

urlpatterns = [
    path("", FilmeListView.as_view(), name="filme_list"),
    path("create/", FilmeCreateView.as_view(), name="filme_create"),
    path("edit/<int:pk>/", FilmeUpdateView.as_view(), name="filme_update"),
    path("delete/<int:pk>/", FilmeDeleteView.as_view(), name="filme_delete")
]
