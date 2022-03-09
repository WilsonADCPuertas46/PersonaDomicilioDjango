from django.db import models

# Create your models here.
class Domicilio(models.Model):
    direccion = models.CharField(max_length=255)
    barrio = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.direccion} {self.barrio} {self.ciudad}'

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # Forma en crear una FK entre una clase a otra
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'
