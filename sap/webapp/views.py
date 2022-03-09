from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido_pe(request):
    no_personas = Persona.objects.count()  # Forma de que nos muestre la cantidad de personas desde la base de datos
    # personas = Persona.objects.all() # Nos regresara todos lo objetos de tipo persona que hay
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas})
    # Esto es uso de temples(plantillas), otra forma de mostrar la informacion


def bienvenido_do(request):
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    return render(request, 'bienvenido2.html' ,{'no_domicilios': no_domicilios, 'domicilios': domicilios})
