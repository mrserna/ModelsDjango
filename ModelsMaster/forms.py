from django.db import models
from django.forms import ModelForm
from .models import Ambito, TipoObjetivo, Estructura, Riesgo

class AmbitoForm(ModelForm):
    class Meta:
        model = Ambito
        fields = ['Str_Nombre', 'Str_Descripcion']

class TipoObjetivoForm(ModelForm):
    class Meta:
        model = TipoObjetivo
        fields = ['Str_Nombre'] 

class EstructuraForm(ModelForm):
    class Meta:
        model = Estructura
        fields = ['Str_Nombre' ]

class RiesgoForm(ModelForm):
    class Meta:
        model = Riesgo
        fields = ['Str_Nombre']
