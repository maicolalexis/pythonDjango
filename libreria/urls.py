#para las urls de nuestas vistas html o views.py
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
'''path('NombreQueSaldraEnElBuscador', views.NombreDelaFuncion, name="nombreDeLaFuncion")'''
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),
    path('Libros', views.Libros, name='libros'),
    path('nosotros', views.nosotros, name="nosotros"),
    path('crearLibro', views.crearLibro, name='crearLibro'),
    path('eliminarLibro/<int:id>', views.eliminarLibro, name='eliminar'),
    path('Libros/editarLibro/<int:id>', views.editarLibro, name='editarLibro'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
'''static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) sirve para las imagenes 
para que todos estos urlpatterns contengan la url de las imagenes'''

