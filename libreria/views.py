from ast import Delete
from django.shortcuts import redirect, render
from .models import Libro
from .forms import libroForm
# Create your views here.
def inicio(request):
    return render(request, "inicio.html")
def Libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, "libros/index.html", {'libros': libros})
def nosotros(request):
    return render(request, "index.html")
def crearLibro(request):
    formulario = libroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, "libros/crear.html", {'formulario': formulario})
def editarLibro(request):
    return render(request, "libros/editar.html")
def eliminarLibro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')