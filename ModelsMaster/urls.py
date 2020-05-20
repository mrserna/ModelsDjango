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

    path('index/tipo_objetivo', views.index_tipo_objetivo),
    path('show/tipo_objetivo/<int:id>', views.show_tipo_objetivo),
    path('new/tipo_objetivo', views.new_tipo_objetivo),
    path('create/tipo_objetivo', views.create_tipo_objetivo),
    path('edit/tipo_objetivo/<int:id>', views.edit_tipo_objetivo),
    path('update/tipo_objetivo/<int:id>', views.update_tipo_objetivo),
    path('delete/tipo_objetivo/<int:id>', views.delete_tipo_objetivo),

    path('index/estructura', views.index_estructura),
    path('show/estructura/<int:id>', views.show_estructura),
    path('new/estructura', views.new_estructura),
    path('create/estructura', views.create_estructura),
    path('edit/estructura/<int:id>', views.edit_estructura),
    path('update/estructura/<int:id>', views.update_estructura),
    path('delete/estructura/<int:id>', views.delete_estructura),

    path('index/riesgo', views.index_riesgo), 
    path('show/riesgo/<int:id>', views.show_riesgo),
    path('new/riesgo', views.new_riesgo),
    path('create/riesgo', views.create_riesgo),
    path('edit/riesgo/<int:id>', views.edit_riesgo),
    path('update/riesgo/<int:id>', views.update_riesgo),
    path('delete/riesgo/<int:id>', views.delete_riesgo),

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