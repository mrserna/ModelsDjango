from django.shortcuts import render, redirect
from django.views import View
from .forms import AmbitoForm, TipoObjetivoForm, EstructuraForm, RiesgoForm, TipoIntervinienteForm, SectorForm, NivelAreaGeograficaForm
from .models import Ambito,TipoObjetivo,Estructura,Riesgo,TipoInterviniente,Sector,NivelAreaGeografica
# Create your views here.
def index(request):
    return render(request, 'index.html')

class AmbitoView(View):
    def index(request):
        all = Ambito.objects.filter(bool_am_eliminado=False)
        args = {
            "ambitos":all
        }
        return render(request, 'Ambitos/index.html', args)

    def show(request,id):
        ambito = Ambito.objects.get(id_am=id)
        args = {
            "ambito":ambito
        }
        return render(request, 'Ambitos/show.html', args)
    
    def new(request):
        return render(request,'Ambitos/new.html')

    def create(request):
        form = AmbitoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "El ambito se ha creado con éxito"
            all = Ambito.objects.filter(bool_am_eliminado=False)
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
        ambito = Ambito.objects.get(id_am=id)
        args = {
            "ambito":ambito
            }
        return render(request, 'Ambitos/edit.html', args)

    def update(request,id):
        ambito = Ambito.objects.get(id_am=id)
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
            ambito = Ambito.objects.get(id_am=id)
            args = {
                "form":form,
                "ambito":ambito
            }
            return render(request, 'Ambitos/edit.html',args)

    def delete(request,id):
        ambito = Ambito.objects.get(id_am=id)
        ambito.bool_am_eliminado = True
        ambito.save()
        eliminado = "El ambito se ha eliminado"
        all = Ambito.objects.filter(bool_am_eliminado=False)
        args = {
            "eliminado":eliminado,
            "ambitos":all
        }
        return render(request, 'Ambitos/index.html', args)

class TipoObjetivoView(View):
    def index(request):
        all = TipoObjetivo.objects.filter(bool_to_eliminado=False)
        args = {
            "tipos_objetivos":all
        }
        return render(request, 'TipoObjetivo/index.html', args)

    def show(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_to=id)
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
            all = TipoObjetivo.objects.filter(bool_to_eliminado=False)
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
        tipo_objetivo = TipoObjetivo.objects.get(id_to=id)
        args = {
            "tipo_objetivo":tipo_objetivo
        }
        return render(request, 'TipoObjetivo/edit.html', args)

    def update(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_to=id)
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
        tipo_objetivo = TipoObjetivo.objects.get(id_to=id)
        tipo_objetivo.bool_to_eliminado = True
        tipo_objetivo.save()
        eliminado = "El tipo objetivo se ha eliminado"
        all = TipoObjetivo.objects.filter(bool_to_eliminado=False)
        args = {
            "eliminado":eliminado,
            "tipos_objetivos":all
        }
        return render(request, 'TipoObjetivo/index.html', args)

class EstructuraView(View):
    def index(request):
        all = Estructura.objects.filter(bool_est_eliminado=False)
        args = {
            "estructuras":all
        }
        return render(request, 'Estructura/index.html', args)

    def show(request,id):
        estructura = Estructura.objects.get(id_est=id)
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
            all = Estructura.objects.filter(bool_est_eliminado=False)
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
        estructura = Estructura.objects.get(id_est=id)
        args = {
            "estructura": estructura
        }
        return render(request, 'Estructura/edit.html', args)

    def update(request,id):
        estructura = Estructura.objects.get(id_est=id)
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
        estructura = Estructura.objects.get(id_est=id)
        estructura.bool_est_eliminado = True
        estructura.save()
        eliminado = "El tipo objetivo se ha eliminado"
        all = Estructura.objects.filter(bool_est_eliminado=False)
        args = {
            "eliminado":eliminado,
            "estructuras":all
        }
        return render(request, 'Estructura/index.html', args)

class RiesgoView(View):
    def index(request):
        all = Riesgo.objects.filter(bool_rg_eliminado=False)
        args = {
            "riesgos":all
        }
        return render(request, 'Riesgo/index.html', args)

    def show(request,id):
        riesgo = Riesgo.objects.get(id_rg=id)
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
            all = Riesgo.objects.filter(bool_rg_eliminado=False)
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
        riesgo = Riesgo.objects.get(id_rg=id)
        args = {
            "riesgo":riesgo
        }
        return render(request, 'Riesgo/edit.html', args)

    def update(request,id):
        riesgo = Riesgo.objects.get(id_rg=id)
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
        riesgo = Riesgo.objects.get(id_rg=id)
        riesgo.bool_rg_eliminado = True
        riesgo.save()
        all = Riesgo.objects.filter(bool_rg_eliminado=False)
        eliminado = "El riesgo se ha eliminado"
        args = {
            "eliminado":eliminado,
            "riesgos":all
        }
        return render(request, 'Riesgo/index.html', args)

class TipoIntervinienteView(View):

    def index(request):
        all = TipoInterviniente.objects.filter(bool_ti_eliminado=False)
        args = {
            "tipo_intervinientes":all
        }
        return render(request, 'TipoInterviniente/index.html', args)

    def show(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_ti=id)
        args = {
            "tipo_interviniente":tipo_interviniente
        }
        return render(request, 'TipoInterviniente/show.html', args)

    def new(request):
        return render(request, 'TipoInterviniente/new.html')

    def create(request):
        ModelForm_form = TipoIntervinienteForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El tipo interviniente se ha creado con éxito!"
            all = TipoInterviniente.objects.filter(bool_ti_eliminado=False)
            args ={
                "aviso":aviso,
                "tipo_intervinientes":all
            }
            return render(request, 'TipoInterviniente/index.html', args)
        else:
            args = {
                "form":ModelForm_form
            }
            return render(request, 'TipoInterviniente/new.html', args)

    def edit(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_ti=id)
        args = {
            "tipo_interviniente":tipo_interviniente
        }
        return render(request, 'TipoInterviniente/edit.html', args)

    def update(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_ti=id)
        ModelForm_form = TipoIntervinienteForm(request.POST, instance=tipo_interviniente)
        if ModelForm_form.is_valid():
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "tipo_interviniente":tipo_interviniente
            }
        else:
            args = {
                "form":ModelForm_form,
                "tipo_interviniente":tipo_interviniente
            }
        return render(request, 'TipoInterviniente/edit.html', args)

    def delete(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_ti=id)
        tipo_interviniente.bool_ti_eliminado = True
        tipo_interviniente.save()
        eliminado = "El tipo Interviniente se ha eliminado"
        all = TipoInterviniente.objects.filter(bool_ti_eliminado=False)
        args = {
            "eliminado":eliminado,
            "tipo_intervinientes":all
        }
        return render(request, 'TipoInterviniente/index.html', args)

class SectorView(View):

    def index(request):
        all = Sector.objects.filter(bool_sc_eliminado=False)
        args = {
            "sectores":all
        }
        return render(request, 'Sector/index.html', args)

    def show(request,id):
        sector = Sector.objects.get(id_sc=id)
        args = {
            "sector":sector
        }
        return render(request, 'Sector/show.html', args)

    def new(request):
        return render(request, 'Sector/new.html')

    def create(request):
        ModelForm_form = SectorForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El sector se ha creado con éxito!"
            all = Sector.objects.filter(bool_sc_eliminado=False)
            args = {
                "aviso":aviso,
                "sectores":all
            }
            return render(request, 'Sector/index.html', args)
        else:
            args = {
                "form":ModelForm_form
            }
            return render(request, 'Sector/new.html', args)
    def edit(request,id):
        sector = Sector.objects.get(id_sc=id)
        args = {
            "sector":sector
        }
        return render(request, 'Sector/edit.html', args)

    def update(request,id):
        sector = Sector.objects.get(id_sc=id)
        ModelForm_form = SectorForm(request.POST, instance=sector)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "sector":sector
            }
        else:
            args = {
                "form":ModelForm_form,
                "sector":sector
            }
        return render(request, 'Sector/edit.html', {"aviso":aviso, "sector":sector})

    def delete(request,id):
        sector = Sector.objects.get(id_sc=id)
        sector.bool_sc_eliminado = True
        sector.save()
        eliminado = "El sector se ha eliminado"
        all = Sector.objects.filter(bool_sc_eliminado=False)
        args = {
            "eliminado":eliminado,
            "sectores":all
        }
        return render(request, 'Sector/index.html', args)

class NivelAreaGeograficaView(View):
    def index(request):
        all = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
        args = {
            "nags":all
        }
        return render(request, 'Nag/index.html', args)

    def show(request,id):
        nag = NivelAreaGeografica.objects.get(id_nag=id)
        args = {
            "nag":nag
        }
        return render(request, 'Nag/show.html', args)

    def new(request):
        return render(request, 'Nag/new.html')

    def create(request):
        ModelForm_form = NivelAreaGeograficaForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Nivel de Área geográfica se ha creado con éxito!"
            all = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
            args = {
                "aviso":aviso,
                "nags":all
            }
            return render(request, 'Nag/index.html', args)
        else:
            args = {
                "form":ModelForm_form
            }
            return render (request, 'Nag/new.html', args)

    def edit(request,id):
        nag = NivelAreaGeografica.objects.get(id_nag=id)
        args = {
            "nag":nag
        }
        return render(request, 'Nag/edit.html', args)

    def update(request,id):
        nag = NivelAreaGeografica.objects.get(id_nag=id)
        ModelForm_form = NivelAreaGeograficaForm(request.POST, instance=nag)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "nag":nag
            }
        else:
            args = {
                "form":ModelForm_form,
                "nag":nag
            }
        return render(request, 'Nag/edit.html', args)

    def delete(request,id):
        nag = NivelAreaGeografica.objects.get(id_nag=id)
        nag.bool_nag_eliminado = True
        nag.save()
        eliminado = "El Nivel de Área geográfica se ha eliminado"
        all = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
        args = {
            "eliminado":eliminado,
            "nags":all
        }
        return render(request, 'Nag/index.html', args)