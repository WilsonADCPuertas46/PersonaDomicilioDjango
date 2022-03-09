from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona, Domicilio


# Esta clase es para crear validaciones a nuestro formulario y tambien personalizar nuestro formulario
class PersonaForm(ModelForm):  # Donde esta estendera de la clase ModelsForm
    class Meta:
        model = Persona  # La clase de modelo con la que vamos a trabajr
        fields = '__all__'  # Los campos de dicha clase modelo uqe vamos a trabajr , __all__ significa todos.
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }  # Con esto lo que hicimos es hacer una validacion al email de nuestro formulario, es decir, a la hora de
        # llenar el espacio de email, cumpla los requisitos, por ejemplo , colocar @


class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'barrio': TextInput(attrs={'type': 'barrio'})
        }

