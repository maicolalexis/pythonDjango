from django import forms
from django import forms
from .models import Libro

class libroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'