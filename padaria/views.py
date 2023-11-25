from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import padaria


class PadariaListView(ListView):
    model = padaria


class PadariaCreateView(CreateView):
    model = padaria
    fields = ["nome", "endereco", "telefone", "dia"]
    success_url = reverse_lazy("padaria_home")


class PadariaUpdateView(UpdateView):
    model = padaria
    fields = ["nome", "endereco", "telefone", "dia"]
    success_url = reverse_lazy("padaria_home")

class PadariaDeleteView(DeleteView):
    model = padaria
    success_url = reverse_lazy("padaria_home")


