from django.contrib import admin

# Register your models here.
from personas.models import Persona, Domicilio

admin.site.register(Persona) # Registrando mi clase modelo de persona
admin.site.register(Domicilio) # Registro de domicilio