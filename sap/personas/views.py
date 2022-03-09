from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.form import PersonaForm, DomicilioForm  # Clase que creamos en el nuevo archivo form
from personas.models import Persona, Domicilio


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalles.html', {'persona': persona})


# PersonaForm = modelform_factory(Persona, exclude=[]) # Fue reemplazado por la clase creada en el archivo form.py

def nuevaPersona(request):
    if request.method == 'POST':  # Comprobación para ver si es de tipo POST y no get asi saber que se esta enviando
        formaPersona = PersonaForm(request.POST)  # Almacenar la informacion del formulario              # la informacio
        if formaPersona.is_valid():  # Validar el formulario donde se dara la informacion
            formaPersona.save()  # Se hara un insert a la DB y se guardara
            return redirect('inicio')  # Volver al inicio cuando la informacion fue mandada y guardada
    else:  # Quiere decir que no se envio la informacion o es 1ra vez que a a enviar
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':  # Comprobación para ver si es de tipo POST y no get asi saber que se esta enviando
        formaPersona = PersonaForm(request.POST,
                                   instance=persona)  # Almacenar la informacion del formulario          # la informacio
        if formaPersona.is_valid():  # Validar el formulario donde se dara la informacion
            formaPersona.save()  # Se hara un update a la DB y se guardara
            return redirect('inicio')  # Ya deves de sabrer porque inicio
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarPersona(request, id):  # Recibir el id a eliminar
    persona = get_object_or_404(Persona, pk=id)  # Recuperamos ese id
    if persona:  # Verificacion si ese id existe
        persona.delete()  # Existe se eliminara
    return redirect('inicio')


def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalle_domicilio.html', {'domicilio': domicilio})


def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('ir_domicilio')
    else:
        formaDomicilio = DomicilioForm

    return render(request, 'domicilios/new_domicilio.html', {'formaDomicilio': formaDomicilio})


def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST,instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('ir_domicilio')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)

    return render(request, 'domicilios/editar_domicilio.html', {'formaDomicilio': formaDomicilio})


def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('ir_domicilio')
