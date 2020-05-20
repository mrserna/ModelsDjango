from django.shortcuts import render, redirect
from django.views import View
from .forms import AmbitoForm, TipoObjetivoForm, EstructuraForm, RiesgoForm
from .models import Ambito,TipoObjetivo,Estructura,Riesgo,TipoInterviniente,Sector,Nivel_Area_Geografica
# Create your views here.
def index(request):
    return render(request, 'index.html')

class AmbitoView(View):
    def index(request):
        all = Ambito.objects.filter(bool_eliminado=False)
        args = {"ambitos":all}
        return render(request, 'Ambitos/index.html', {"ambitos":all})

    def show(request,id):
        ambito = Ambito.objects.get(id_Ambito=id)
        return render(request, 'Ambitos/show.html', {"ambito":ambito})
    
    def new(request):
        return render(request,'Ambitos/new.html')

    def create(request):
        form = AmbitoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "El ambito se ha creado con éxito"
            all = Ambito.objects.filter(bool_eliminado=False)
            args = {
                "aviso":aviso,
                "ambitos":all
                }
            return render(request, 'Ambitos/index.html', args )
        else:
            args = {
                'form': form
                }
            return render (request, 'Ambitos/new.html', args )

    def edit(request,id):
        ambito = Ambito.objects.get(id_Ambito=id)
        args = {
            "ambito":ambito
            }
        return render(request, 'Ambitos/edit.html', args)

    def update(request,id):
        ambito = Ambito.objects.get(id_Ambito=id)
        form = AmbitoForm(request.POST, instance=ambito)
        if form.is_valid():
            form.save()
            aviso = "Se han actualizado los datos"
            args = {
                "aviso":aviso,
                "form":form,
                "ambito":ambito
            }
            return render(request, 'Ambitos/edit.html', args)
        else:
            ambito = Ambito.objects.get(id_Ambito=id)
            args = {
                "form":form,
                "ambito":ambito
            }
            return render(request, 'Ambitos/edit.html',args)

    def delete(request,id):
        ambito = Ambito.objects.get(id_Ambito=id)
        ambito.bool_eliminado = True
        ambito.save()
        eliminado = "El ambito se ha eliminado"
        all = Ambito.objects.filter(bool_eliminado=False)
        args = {
            "eliminado":eliminado,
            "ambitos":all
        }
        return render(request, 'Ambitos/index.html', args)

class TipoObjetivoView(View):
    def index(request):
        all = TipoObjetivo.objects.filter(bool_eliminado=False)
        args = {
            "tipos_objetivos":all
        }
        return render(request, 'TipoObjetivo/index.html', args)

    def show(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo = id)
        args = {
            "tipo_objetivo":tipo_objetivo
        }
        return render(request, 'TipoObjetivo/show.html', args)

    def new(request):
        return render(request, 'TipoObjetivo/new.html')

    def create(request):
        form = TipoObjetivoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "El tipo objetivo se ha creado con éxito"
            all = TipoObjetivo.objects.filter(bool_eliminado=False)
            args = {
                "aviso":aviso,
                "tipos_objetivos":all
            }
            return render(request, 'TipoObjetivo/index.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'TipoObjetivo/new.html', args)

    def edit(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)
        args = {
            "tipo_objetivo":tipo_objetivo
        }
        return render(request, 'TipoObjetivo/edit.html', args)

    def update(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)
        form = TipoObjetivoForm(request.POST, instance = tipo_objetivo)
        if form.is_valid():
            form.save()
            aviso = "Los datos se han actualizado!"
            args = {
                "aviso":aviso,
                "form":form,
                "tipo_objetivo":tipo_objetivo
            }
            return render(request, 'TipoObjetivo/edit.html', args)
        else:
            args = {
                "form":form,
                "tipo_objetivo":tipo_objetivo
            }
            return render(request, 'TipoObjetivo/edit.html', args)

    def delete(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)
        tipo_objetivo.bool_eliminado = True
        tipo_objetivo.save()
        eliminado = "El tipo objetivo se ha eliminado"
        all = TipoObjetivo.objects.filter(bool_eliminado=False)
        args = {
            "eliminado":eliminado,
            "tipos_objetivos":all
        }
        return render(request, 'TipoObjetivo/index.html', args)

class EstructuraView(View):
    def index(request):
        all = Estructura.objects.filter(bool_eliminado=False)
        args = {
            "estructuras":all
        }
        return render(request, 'Estructura/index.html', args)

    def show(request,id):
        estructura = Estructura.objects.get(id_Estructura=id)
        args = {
            "estructura":estructura
        }
        return render(request, 'Estructura/show.html', args)

    def new(request):
        return render(request, 'Estructura/new.html')

    def create(request):
        form = EstructuraForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "La estructura se ha creado con éxito"
            all = Estructura.objects.filter(bool_eliminado=False)
            args = {
                "aviso":aviso,
                "estructuras":all
            }
            return render(request, 'Estructura/index.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'Estructura/new.html', args)

    def edit(request,id):
        estructura = Estructura.objects.get(id_Estructura=id)
        args = {
            "estructura": estructura
        }
        return render(request, 'Estructura/edit.html', args)

    def update(request,id):
        estructura = Estructura.objects.get(id_Estructura=id)
        form = EstructuraForm(request.POST, instance=estructura)
        if form.is_valid():
            form.save()
            aviso = "Los datos se han actualizado!"
            args = {
                "aviso":aviso,
                "estructura":estructura
            }
            return render(request, 'Estructura/edit.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'Estructura/edit.html', args)

    def delete(request,id):
        estructura = Estructura.objects.get(id_Estructura=id)
        estructura.bool_eliminado = True
        estructura.save()
        eliminado = "El tipo objetivo se ha eliminado"
        all = Estructura.objects.filter(bool_eliminado=False)
        args = {
            "eliminado":eliminado,
            "estructuras":all
        }
        return render(request, 'Estructura/index.html', args)

class RiesgoView(View):
    def index(request):
        all = Riesgo.objects.filter(bool_eliminado=False)
        args = {
            "riesgos":all
        }
        return render(request, 'Riesgo/index.html', args)

    def show(request,id):
        riesgo = Riesgo.objects.get(id_Riesgo=id)
        args = {
            "riesgo":riesgo
        }
        return render(request, 'Riesgo/show.html', args)

    def new(request):
        return render(request, 'Riesgo/new.html')

    def create(request):
        form = RiesgoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "El riesgo se ha creado con éxito"
            all = Riesgo.objects.filter(bool_eliminado=False)
            args = {
                "aviso":aviso,
                "riesgos":all
            }
            return render(request, 'Riesgo/index.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'Riesgo/new.html', args)

    def edit(request,id):
        riesgo = Riesgo.objects.get(id_Riesgo=id)
        args = {
            "riesgo":riesgo
        }
        return render(request, 'Riesgo/edit.html', args)

    def update(request,id):
        riesgo = Riesgo.objects.get(id_Riesgo=id)
        form = RiesgoForm(request.POST, instance=riesgo)
        if form.is_valid():
            form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "riesgo":riesgo
            }
            return render(request, 'Riesgo/edit.html', args)
        else:
            args = {
                "riesgo":riesgo,
                "form":form
            }
            return render(request, 'Riesgo/edit.html', args)

    def delete(request,id):
        riesgo = Riesgo.objects.get(id_Riesgo=id)
        riesgo.bool_eliminado = True
        riesgo.save()
        all = Riesgo.objects.filter(bool_eliminado=False)
        eliminado = "El riesgo se ha eliminado"
        args = {
            "eliminado":eliminado,
            "riesgos":all
        }
        return render(request, 'Riesgo/index.html', args)

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

def index_sector(request):
    all = Sector.objects.filter(bool_Sc_eliminado=False)
    return render(request, 'Sector/index.html', {"sectores":all})

def show_sector(request,id):
    sector = Sector.objects.get(id_Sector=id)
    return render(request, 'Sector/show.html', {"sector":sector})

def new_sector(request):
    return render(request, 'Sector/new.html')

def create_sector(request):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    sector = Sector(Str_Sc_Nombre = nombre, Str_Sc_Descripcion=descripcion)
    sector.save()
    aviso = "El sector se ha creado con éxito!"

    all = Sector.objects.filter(bool_Sc_eliminado=False)
    return render(request, 'Sector/index.html', {"aviso":aviso, "sectores":all})

def edit_sector(request,id):
    sector = Sector.objects.get(id_Sector=id)
    return render(request, 'Sector/edit.html', {"sector":sector})

def update_sector(request,id):
    sector = Sector.objects.get(id_Sector=id)
    sector.Str_Sc_Nombre = request.POST['nombre']
    sector.Str_Sc_Descripcion = request.POST['descripcion']
    sector.save()
    aviso = "Los datos se han actualizado con éxito"

    return render(request, 'Sector/edit.html', {"aviso":aviso, "sector":sector})

def delete_sector(request,id):
    sector = Sector.objects.get(id_Sector=id)
    sector.bool_eliminado = True
    sector.save()
    eliminado = "El sector se ha eliminado"
    all = Sector.objects.filter(bool_Sc_eliminado=False)

    return render(request, 'Sector/index.html', {"eliminado":eliminado, "sectores":all})

def index_nag(request):
    all = Nivel_Area_Geografica.objects.filter(bool_NG_Eliminado=False)
    return render(request, 'Nag/index.html', {"nags":all})

def show_nag(request,id):
    nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
    return render(request, 'Nag/show.html', {"nag":nag})

def new_nag(request):
    return render(request, 'Nag/new.html')

def create_nag(request):
    nivel = request.POST.get('nivel_area')
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    nag = Nivel_Area_Geografica(Num_NG_Nivel=nivel,Str_NG_Nombre = nombre, Str_NG_Descripcion=descripcion)
    nag.save()
    aviso = "El Nivel de Área geográfica se ha creado con éxito!"

    all = Nivel_Area_Geografica.objects.filter(bool_NG_Eliminado=False)
    return render(request, 'Nag/index.html', {"aviso":aviso, "nags":all})

def edit_nag(request,id):
    nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
    return render(request, 'Nag/edit.html', {"nag":nag})

def update_nag(request,id):
    nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
    nag.Str_NG_Nombre = request.POST['nombre']
    nag.Str_NG_Descripcion = request.POST['descripcion']
    nag.Num_NG_Nivel = request.POST.get('nivel_area')
    nag.save()
    aviso = "Los datos se han actualizado con éxito"

    return render(request, 'Nag/edit.html', {"aviso":aviso, "nag":nag})

def delete_nag(request,id):
    nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
    nag.bool_NG_Eliminado = True
    nag.save()
    eliminado = "El Nivel de Área geográfica se ha eliminado"
    all = Nivel_Area_Geografica.objects.filter(bool_NG_Eliminado=False)

    return render(request, 'Nag/index.html', {"eliminado":eliminado, "nags":all})