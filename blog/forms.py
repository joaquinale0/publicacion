from django import forms
from django.forms import ModelForm
from .models import *

class CrearPoster(forms.ModelForm):
    class Meta:
        model = contenido
        fields = ["nombre","apellido","Titulo","imagen","descripcion"]

    apellido = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)