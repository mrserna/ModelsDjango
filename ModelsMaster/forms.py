from django.db import models
from django.forms import ModelForm
from .models import Ambito, TipoObjetivo, Estructura, Riesgo, TipoInterviniente, Sector, NivelAreaGeografica

class AmbitoForm(ModelForm):
    class Meta:
        model = Ambito
        fields = ['str_am_nombre', 'str_am_descripcion']

class TipoObjetivoForm(ModelForm):
    class Meta:
        model = TipoObjetivo
        fields = ['str_to_nombre'] 

class EstructuraForm(ModelForm):
    class Meta:
        model = Estructura
        fields = ['str_est_nombre' ]

class RiesgoForm(ModelForm):
    class Meta:
        model = Riesgo
        fields = ['str_rg_nombre']

class TipoIntervinienteForm(ModelForm):
    class Meta:
        model = TipoInterviniente
        fields = ['str_ti_nombre']

class SectorForm(ModelForm):
    class Meta:
        model = Sector
        fields = ['str_sc_nombre', 'str_sc_descripcion']

class NivelAreaGeograficaForm(ModelForm):
    class Meta:
        model = NivelAreaGeografica
        fields = ['num_nag_nivel', 'str_nag_nombre', 'str_nag_descripcion']
