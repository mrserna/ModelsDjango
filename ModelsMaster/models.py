from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Ambito(models.Model):
    id_Ambito=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256, null=False, blank=False)
    #Str_Nombre=models.CharField(max_length=256, null=False, blank=False, db_column="Nombre")
    Str_Descripcion=models.CharField(max_length=256, null=True, blank=True)
    bool_eliminado=models.BooleanField(default=False)

    class Meta:
        db_table = "ambitos"

class TipoObjetivo(models.Model):
    id_Tipo_Objetivo=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256, null=False, blank=False)
    bool_eliminado=models.BooleanField(default=False)

    class Meta:
        db_table = "tipo_objetivos"

class Estructura(models.Model):
    id_Estructura=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256)
    bool_eliminado=models.BooleanField(default=False)

    class Meta:
        db_table = "estructuras"

class Riesgo(models.Model):
    id_Riesgo=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256)
    bool_eliminado=models.BooleanField(default=False)

    class Meta:
        db_table = "riesgos"

class TipoInterviniente(models.Model):
    id_Tipo_Interviniente=models.AutoField(primary_key=True)
    Str_Nombre=models.CharField(max_length=256)
    bool_eliminado=models.BooleanField(default=False)

    class Meta:
        db_table = "tipo_intervinientes"

class Sector(models.Model):
    id_Sector=models.AutoField(primary_key=True)
    Str_Sc_Nombre=models.CharField(max_length=256)
    Str_Sc_Descripcion=models.CharField(max_length=256)
    bool_Sc_eliminado=models.BooleanField(default=False)

    class Meta:
        db_table = "sectores"

class Nivel_Area_Geografica(models.Model):
    id_Nivel_Area=models.AutoField(primary_key=True)
    Num_NG_Nivel=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)],null=False,blank=False)
    Str_NG_Nombre=models.CharField(max_length=256,null=False,blank=False)
    Str_NG_Descripcion=models.CharField(max_length=256,null=True,blank=True)
    bool_NG_Eliminado=models.BooleanField(default=False)

    class Meta:
        db_table = "nivel_areas_geograficas"