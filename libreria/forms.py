from django import forms
from django import forms
from .models import Libro
#para mostrar todos los datos en el formulario ejemplo
'''si es un una imagen le va a mostrar lo siguiente:

<input 
      type="de que tipo es" 
       name="name" 
       placeholder="texto"
       value="y el valor que tiene">
    </div>
'''
class libroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'