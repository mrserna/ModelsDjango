from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Ambito(models.Model):
    id_am=models.AutoField(primary_key=True, db_column="id_Ambito")
    #Str_Nombre=models.CharField(max_length=256, null=False, blank=False)
    str_am_nombre=models.CharField(max_length=256, null=False, blank=False, db_column="Nombre")
    str_am_descripcion=models.CharField(max_length=256, null=True, blank=True, db_column="Descripcion")
    bool_am_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "ambitos"

class TipoObjetivo(models.Model):
    id_to=models.AutoField(primary_key=True, db_column="id_Tipo_Objetivo")
    str_to_nombre=models.CharField(max_length=256, null=False, blank=False, db_column="Nombre")
    bool_to_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "tipo_objetivos"

class Estructura(models.Model):
    id_est=models.AutoField(primary_key=True, db_column="id_Estructura")
    str_est_nombre=models.CharField(max_length=256, db_column="Nombre")
    bool_est_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "estructuras"

class Riesgo(models.Model):
    id_rg=models.AutoField(primary_key=True, db_column="id_Riesgo")
    str_rg_nombre=models.CharField(max_length=256,db_column="Nombre")
    bool_rg_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "riesgos"

class TipoInterviniente(models.Model):
    id_ti=models.AutoField(primary_key=True, db_column="id_Tipo_Interviniente")
    str_ti_nombre=models.CharField(max_length=256, db_column="Nombre")
    bool_ti_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "tipo_intervinientes"

class Sector(models.Model):
    id_sc=models.AutoField(primary_key=True, db_column="id_Sector")
    str_sc_nombre=models.CharField(max_length=256, db_column="Nombre")
    str_sc_descripcion=models.CharField(max_length=256, db_column="Descripcion",null=True, blank=True)
    bool_sc_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "sectores"

class NivelAreaGeografica(models.Model):
    id_nag=models.AutoField(primary_key=True, db_column="id_Nivel_Area")
    num_nag_nivel=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)],null=False,blank=False, db_column="Nivel")
    str_nag_nombre=models.CharField(max_length=256,null=False,blank=False, db_column="Nombre")
    str_nag_descripcion=models.CharField(max_length=256,null=True,blank=True, db_column="Descripcion")
    bool_nag_eliminado=models.BooleanField(default=False, db_column="eliminado")

    class Meta:
        db_table = "nivel_areas_geograficas"