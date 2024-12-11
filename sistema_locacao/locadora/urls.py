from django.urls import path
from .views import (
    home,
    ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    FilmeListView, FilmeDetailView, FilmeCreateView, FilmeUpdateView, FilmeDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/novo/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/excluir/', ClienteDeleteView.as_view(), name='cliente-delete'),
    path('filmes/', FilmeListView.as_view(), name='filme-list'),
    path('filmes/novo/', FilmeCreateView.as_view(), name='filme-create'),
    path('filmes/<int:pk>/', FilmeDetailView.as_view(), name='filme-detail'),
    path('filmes/<int:pk>/editar/', FilmeUpdateView.as_view(), name='filme-update'),
    path('filmes/<int:pk>/excluir/', FilmeDeleteView.as_view(), name='filme-delete'),
]


