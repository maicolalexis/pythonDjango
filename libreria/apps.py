#se crea automaticamente al crear la app
'''python manage.py startapp nombredelaapp'''
from django.apps import AppConfig


class LibreriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'libreria'
