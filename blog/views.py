from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import  ListView, CreateView, View
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *

class InicioBlog(ListView):
    model = contenido
    # paginate_by = 10
    queryset = contenido.objects.all().order_by('-id')
    template_name = 'blog.html'
    context_object_name = "contenidos"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Blog"
        return context
    
class CrearPosterVista(CreateView):
    model = contenido
    form_class = CrearPoster
    template_name = 'agregarFoto.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Poster"
        return context