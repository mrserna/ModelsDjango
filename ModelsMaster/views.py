from django.shortcuts import render
from ModelsMaster.models import Ambitos,TipoObjetivo
# Create your views here.

def index(request):
    return render(request, 'index.html')

def index_ambito(request):
    if Ambitos.objects.filter(bool_eliminado=False).exists():
        all = Ambitos.objects.filter(bool_eliminado=False)
        return render(request, 'Ambitos/index.html', {"ambitos":all})
    else:
        return render(request, 'Ambitos/index.html')

def show_ambito(request,id):
    ambito = Ambitos.objects.get(id_Ambito=id)
    return render(request, 'Ambitos/show.html', {"ambito":ambito})

def new_ambito(request):
    return render(request,'Ambitos/new.html')

def create_ambito(request):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']

    ambito=Ambitos(Str_Nombre=nombre,Str_Descripcion=descripcion)
    ambito.save()

    all = Ambitos.objects.filter(bool_eliminado=False)
    return render(request, 'Ambitos/index.html', {"ambitos":all})

def edit_ambito(request,id):
    ambito = Ambitos.objects.get(id_Ambito=id)
    return render(request, 'Ambitos/edit.html', {"ambito":ambito})

def update_ambito(request,id):
    nombre = request.POST["nombre"]
    descripcion = request.POST['descripcion']
    
    ambito = Ambitos.objects.get(id_Ambito=id)
    ambito.Str_Nombre = nombre
    ambito.Str_Descripcion = descripcion
    ambito.save()
    aviso = "Se han actualizado los datos"
    return render(request, 'Ambitos/edit.html', {"aviso":aviso, "ambito":ambito})

def delete_ambito(request,id):
    ambito = Ambitos.objects.get(id_Ambito=id)
    ambito.bool_eliminado = True
    ambito.save()
    eliminado = "El ambito se ha eliminado"
    return render(request, 'Ambitos/index.html', {"eliminado":eliminado,"ambito":ambito})

def index_tipo_objetivo(request):
    all = TipoObjetivo.objects.filter(bool_eliminado=False)
    return render(request, 'TipoObjetivo/index.html', {"tipos_objetivos":all})

def show_tipo_objetivo(request,id):
    tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo = id)
    return render(request, 'TipoObjetivo/show.html', {"tipo_objetivo":tipo_objetivo})

def new_tipo_objetivo(request):
    return render(request, 'TipoObjetivo/new.html')

def create_tipo_objetivo(request):
    nombre = request.POST['nombre']

    tipo_objetivo = TipoObjetivo(Str_Nombre=nombre)
    tipo_objetivo.save()
    aviso = "El tipo objetivo se ha creado con éxito"

    all = TipoObjetivo.objects.filter(bool_eliminado=False)
    return render(request, 'TipoObjetivo/index.html', {"aviso":aviso, "tipos_objetivos":all})

def edit_tipo_objetivo(request,id):
    tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)

    return render(request, 'TipoObjetivo/edit.html', {"tipo_objetivo":tipo_objetivo})

def update_tipo_objetivo(request,id):
    nombre = request.POST['nombre']

    tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)
    tipo_objetivo.Str_Nombre = nombre
    tipo_objetivo.save()
    aviso = "Los datos se han actualizado!"
    
    return render(request, 'TipoObjetivo/edit.html', {"aviso":aviso, "tipo_objetivo":tipo_objetivo})

def delete_tipo_objetivo(request,id):
    tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)
    tipo_objetivo.bool_eliminado = True
    tipo_objetivo.save()
    eliminado = "El tipo objetivo se ha eliminado"
    return render(request, 'TipoObjetivo/index.html', {"eliminado":eliminado,"tipo_objetivo":tipo_objetivo})
