from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from .views import *
from . import views
urlpatterns = [
    path('index/ambito/', views.AmbitoView.index),
    path('show/ambito/<int:id>', views.AmbitoView.show),
    path('new/ambito', views.AmbitoView.new),
    path('create/ambito', views.AmbitoView.create),
    path('edit/ambito/<int:id>', views.AmbitoView.edit),
    path('update/ambito/<int:id>', views.AmbitoView.update),
    path('delete/ambito/<int:id>', views.AmbitoView.delete),

    path('index/tipo_objetivo', views.TipoObjetivoView.index),
    path('show/tipo_objetivo/<int:id>', views.TipoObjetivoView.show),
    path('new/tipo_objetivo', views.TipoObjetivoView.new),
    path('create/tipo_objetivo', views.TipoObjetivoView.create),
    path('edit/tipo_objetivo/<int:id>', views.TipoObjetivoView.edit),
    path('update/tipo_objetivo/<int:id>', views.TipoObjetivoView.update),
    path('delete/tipo_objetivo/<int:id>', views.TipoObjetivoView.delete),

    path('index/estructura', views.EstructuraView.index),
    path('show/estructura/<int:id>', views.EstructuraView.show),
    path('new/estructura', views.EstructuraView.new),
    path('create/estructura', views.EstructuraView.create),
    path('edit/estructura/<int:id>', views.EstructuraView.edit),
    path('update/estructura/<int:id>', views.EstructuraView.update),
    path('delete/estructura/<int:id>', views.EstructuraView.delete),

    path('index/riesgo', views.RiesgoView.index), 
    path('show/riesgo/<int:id>', views.RiesgoView.show),
    path('new/riesgo', views.RiesgoView.new),
    path('create/riesgo', views.RiesgoView.create),
    path('edit/riesgo/<int:id>', views.RiesgoView.edit),
    path('update/riesgo/<int:id>', views.RiesgoView.update),
    path('delete/riesgo/<int:id>', views.RiesgoView.delete),

    path('index/tipo_interviniente', views.TipoIntervinienteView.index),
    path('show/tipo_interviniente/<int:id>', views.TipoIntervinienteView.show),
    path('new/tipo_interviniente', views.TipoIntervinienteView.new),
    path('create/tipo_interviniente', views.TipoIntervinienteView.create),
    path('edit/tipo_interviniente/<int:id>', views.TipoIntervinienteView.edit),
    path('update/tipo_interviniente/<int:id>', views.TipoIntervinienteView.update),
    path('delete/tipo_interviniente/<int:id>', views.TipoIntervinienteView.delete),

    path('index/sector', views.SectorView.index),
    path('show/sector/<int:id>', views.SectorView.show),
    path('new/sector', views.SectorView.new),
    path('create/sector', views.SectorView.create),
    path('edit/sector/<int:id>', views.SectorView.edit),
    path('update/sector/<int:id>', views.SectorView.update),
    path('delete/sector/<int:id>', views.SectorView.delete),

    path('index/nag', views.NivelAreaGeograficaView.index),
    path('show/nag/<int:id>', views.NivelAreaGeograficaView.show),
    path('new/nag', views.NivelAreaGeograficaView.new),
    path('create/nag', views.NivelAreaGeograficaView.create),
    path('edit/nag/<int:id>', views.NivelAreaGeograficaView.edit),
    path('update/nag/<int:id>', views.NivelAreaGeograficaView.update),
    path('delete/nag/<int:id>', views.NivelAreaGeograficaView.delete),
]

urlpatterns += staticfiles_urlpatterns()