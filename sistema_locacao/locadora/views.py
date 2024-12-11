from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Filme

def home(request):
    return render(request, 'locadora/home.html')

class ClienteListView(ListView):
    model = Cliente
    template_name = 'locadora/cliente_list.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'locadora/cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'email']
    template_name = 'locadora/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'email']
    template_name = 'locadora/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'locadora/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')

class FilmeListView(ListView):
    model = Filme
    template_name = 'locadora/filme_list.html'

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'locadora/filme_detail.html'

class FilmeCreateView(CreateView):
    model = Filme
    fields = ['titulo', 'genero', 'ano_lancamento', 'cliente']
    template_name = 'locadora/filme_form.html'
    success_url = reverse_lazy('filme-list')

class FilmeUpdateView(UpdateView):
    model = Filme
    fields = ['titulo', 'genero', 'ano_lancamento', 'cliente']
    template_name = 'locadora/filme_form.html'
    success_url = reverse_lazy('filme-list')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'locadora/filme_confirm_delete.html'
    success_url = reverse_lazy('filme-list')
