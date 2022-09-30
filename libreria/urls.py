from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Libros', views.Libros, name='libros'),
    path('nosotros', views.nosotros, name="nosotros"),
    path('crearLibro', views.crearLibro, name='crearLibro')
]
