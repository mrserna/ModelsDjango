"""ModelsDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ModelsMaster import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    path('new/ambito', views.new_ambito),
    path('create/ambito', views.create_ambito),
    path('index/ambito', views.index_ambito),
    path('show/ambito/<int:id>', views.show_ambito),
    path('edit/ambito/<int:id>',views.edit_ambito),
    path('update/ambito/<int:id>',views.update_ambito),
    path('delete/ambito/<int:id>',views.delete_ambito),

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


]
