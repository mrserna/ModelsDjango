from django.db import models

# Create your models here.
class Ambitos(models.Model):
    id_Ambito=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256, null=False, blank=False)
    Str_Descripcion=models.CharField(max_length=256, null=True, blank=True)
    bool_eliminado=models.BooleanField(default=False)

class TipoObjetivo(models.Model):
    id_Tipo_Objetivo=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256, null=False, blank=False)
    bool_eliminado=models.BooleanField(default=False)

class Estructura(models.Model):
    id_Estructura=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256)
    bool_eliminado=models.BooleanField(default=False)

class Riesgo(models.Model):
    id_Riesgo=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256)
    bool_eliminado=models.BooleanField(default=False)