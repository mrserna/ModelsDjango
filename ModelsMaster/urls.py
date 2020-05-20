from django.contrib import admin
from django.urls import path, include
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

    path('index/tipo_interviniente', views.index_tipo_interviniente),
    path('show/tipo_interviniente/<int:id>', views.show_tipo_interviniente),
    path('new/tipo_interviniente', views.new_tipo_interviniente),
    path('create/tipo_interviniente', views.create_tipo_interviniente),
    path('edit/tipo_interviniente/<int:id>', views.edit_tipo_interviniente),
    path('update/tipo_interviniente/<int:id>', views.update_tipo_interviniente),
    path('delete/tipo_interviniente/<int:id>', views.delete_tipo_interviniente),

    path('index/sector', views.index_sector),
    path('show/sector/<int:id>', views.show_sector),
    path('new/sector', views.new_sector),
    path('create/sector', views.create_sector),
    path('edit/sector/<int:id>', views.edit_sector),
    path('update/sector/<int:id>', views.update_sector),
    path('delete/sector/<int:id>', views.delete_sector),

    path('index/nag', views.index_nag),
    path('show/nag/<int:id>', views.show_nag),
    path('new/nag', views.new_nag),
    path('create/nag', views.create_nag),
    path('edit/nag/<int:id>', views.edit_nag),
    path('update/nag/<int:id>', views.update_nag),
    path('delete/nag/<int:id>', views.delete_nag),
]