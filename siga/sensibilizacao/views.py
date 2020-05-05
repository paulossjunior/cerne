from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Palestra

class PalestraListView(generic.ListView):
    model = Palestra
    context_object_name = 'palestras_list'
    template_name = 'sensibilizacao/palestra_list.html'

class PalestraDetailView(generic.DetailView):
    model = Palestra

class PalestraCreate(CreateView):
    model = Palestra
    fields = '__all__'
    success_url = reverse_lazy('palestras')

class PalestraUpdate(UpdateView):
    model = Palestra
    fields = '__all__'
    success_url = reverse_lazy('palestras')
    
class PalestraDelete(DeleteView):
    model = Palestra
    success_url = reverse_lazy('palestras')