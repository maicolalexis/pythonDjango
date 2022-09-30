from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, "inicio.html")
def Libros(request):
    return render(request, "libros/index.html")
def nosotros(request):
    return render(request, "index.html")
def crearLibro(request):
    return render(request, "libros/crear.html");