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
]
