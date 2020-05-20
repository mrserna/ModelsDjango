from django.db import models
from django.forms import ModelForm
from .models import Ambito, TipoObjetivo

class AmbitoForm(ModelForm):
    class Meta:
        model = Ambito
        fields = ['Str_Nombre', 'Str_Descripcion']

class TipoObjetivoForm(ModelForm):
    class Meta:
        model = TipoObjetivo
        fields = ['Str_Nombre'] 
