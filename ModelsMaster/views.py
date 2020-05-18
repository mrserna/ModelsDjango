from django.shortcuts import render
from ModelsMaster.models import Ambitos,TipoObjetivo,Estructura,Riesgo,TipoInterviniente
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

def index_estructura(request):
    all = Estructura.objects.filter(bool_eliminado=False)
    return render(request, 'Estructura/index.html', {"estructuras":all})

def show_estructura(request,id):
    estructura = Estructura.objects.get(id_Estructura=id)
    return render(request, 'Estructura/show.html', {"estructura":estructura})

def new_estructura(request):
    return render(request, 'Estructura/new.html')

def create_estructura(request):
    nombre = request.POST['nombre']
    estructura = Estructura(Str_Nombre=nombre)
    estructura.save()
    aviso = "La estructura se ha creado con éxito"
    all = Estructura.objects.filter(bool_eliminado=False)

    return render(request, 'Estructura/index.html', {"aviso":aviso, "estructuras":all})

def edit_estructura(request,id):
    estructura = Estructura.objects.get(id_Estructura=id)
    return render(request, 'Estructura/edit.html', {"estructura":estructura})

def update_estructura(request,id):
    estructura = Estructura.objects.get(id_Estructura=id)
    nombre = request.POST['nombre']
    estructura.Str_Nombre = nombre
    estructura.save()
    aviso = "Los datos se han actualizado!"

    return render(request, 'Estructura/edit.html', {"aviso":aviso, "estructura":estructura})

def delete_estructura(request,id):
    estructura = Estructura.objects.get(id_Estructura=id)
    estructura.bool_eliminado = True
    estructura.save()
    eliminado = "El tipo objetivo se ha eliminado"
    all = Estructura.objects.filter(bool_eliminado=False)

    return render(request, 'Estructura/index.html', {"eliminado":eliminado, "estructuras":all})

def index_riesgo(request):
    all = Riesgo.objects.filter(bool_eliminado=False)
    return render(request, 'Riesgo/index.html', {"riesgos":all})

def show_riesgo(request,id):
    riesgo = Riesgo.objects.get(id_Riesgo=id)
    return render(request, 'Riesgo/show.html', {"riesgo":riesgo})

def new_riesgo(request):
    return render(request, 'Riesgo/new.html')

def create_riesgo(request):
    nombre = request.POST['nombre']

    riesgo = Riesgo(Str_Nombre=nombre)
    riesgo.save()
    aviso = "El riesgo se ha creado con éxito"
    all = Riesgo.objects.filter(bool_eliminado=False)
    return render(request, 'Riesgo/index.html', {"aviso":aviso, "riesgos":all})

def edit_riesgo(request,id):
    riesgo = Riesgo.objects.get(id_Riesgo=id)
    return render(request, 'Riesgo/edit.html', {"riesgo":riesgo})

def update_riesgo(request,id):
    riesgo = Riesgo.objects.get(id_Riesgo=id)
    riesgo.Str_Nombre = request.POST['nombre']
    riesgo.save()
    aviso = "Los datos se han actualizado con éxito"
    return render(request, 'Riesgo/edit.html', {"riesgo":riesgo, "aviso":aviso})

def delete_riesgo(request,id):
    riesgo = Riesgo.objects.get(id_Riesgo=id)
    riesgo.bool_eliminado = True
    riesgo.save()
    all = Riesgo.objects.filter(bool_eliminado=False)
    eliminado = "El riesgo se ha eliminado"
    return render(request, 'Riesgo/index.html', {"eliminado":eliminado, "riesgos":all})

def index_tipo_interviniente(request):
    all = TipoInterviniente.objects.filter(bool_eliminado=False)
    return render(request, 'TipoInterviniente/index.html', {"tipo_intervinientes":all})

def show_tipo_interviniente(request,id):
    tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
    return render(request, 'TipoInterviniente/show.html', {"tipo_interviniente":tipo_interviniente})

def new_tipo_interviniente(request):
    return render(request, 'TipoInterviniente/new.html')

def create_tipo_interviniente(request):
    nombre = request.POST['nombre']
    tipo_interviniente = TipoInterviniente(Str_Nombre = nombre)
    tipo_interviniente.save()
    aviso = "El tipo interviniente se ha creado con éxito!"

    all = TipoInterviniente.objects.filter(bool_eliminado=False)
    return render(request, 'TipoInterviniente/index.html', {"aviso":aviso, "tipo_intervinientes":all})

def edit_tipo_interviniente(request,id):
    tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
    return render(request, 'TipoInterviniente/edit.html', {"tipo_interviniente":tipo_interviniente})

def update_tipo_interviniente(request,id):
    tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
    tipo_interviniente.Str_Nombre = request.POST['nombre']
    tipo_interviniente.save()
    aviso = "Los datos se han actualizado con éxito"

    return render(request, 'TipoInterviniente/edit.html', {"aviso":aviso, "tipo_interviniente":tipo_interviniente})

def delete_tipo_interviniente(request,id):
    tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
    tipo_interviniente.bool_eliminado = True
    tipo_interviniente.save()
    eliminado = "El tipo Interviniente se ha eliminado"
    all = TipoInterviniente.objects.filter(bool_eliminado=False)

    return render(request, 'TipoInterviniente/index.html', {"eliminado":eliminado, "tipo_intervinientes":all})