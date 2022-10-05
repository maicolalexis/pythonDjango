from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Libros', views.Libros, name='libros'),
    path('nosotros', views.nosotros, name="nosotros"),
    path('crearLibro', views.crearLibro, name='crearLibro'),
    path('editarLibro', views.editarLibro, name='editarLibro'),
    path('eliminarLibro/<int:id>', views.eliminarLibro, name='eliminar')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)