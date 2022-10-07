#para crear el rol de administrador en la que mostrara toda la vista como un administrador
'''sin necesidad de que nosotros hagamos html'''
from atexit import register
from django.contrib import admin
from .models import Libro
# Register your models here.
admin.site.register(Libro)