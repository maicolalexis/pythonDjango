from ast import Delete
from django.shortcuts import redirect, render
#para obtener los datos de el modelo
from .models import Libro
#para obtener los datos de el formulario
from .forms import libroForm
# Create your views here.


'''para mostrar la vista inicio de la aplicacion'''
def inicio(request):
    return render(request, "inicio.html")



'''para mostrar la vista de libros'''
def Libros(request):
    '''se toman todos los valores que contenga libro'''
    libros = Libro.objects.all() 
    print(libros)#[<Libro: titulo: maiCOL-Descripcion jajajaajaaj>, <Libro: titulo: maicol-Descripcion 1234>]>
    #muestra el objeto que con sus valores que en el html ya se recorreria con un for y se mostrarian
    return render(request, "libros/index.html", {'libros': libros})



#vista de nosotros
def nosotros(request):
    #retorna la vista
    return render(request, "nosotros.html")


#vista de crear el libro
def crearLibro(request):
    #para tomar los datos de el formulario
    formulario = libroForm(request.POST or None, request.FILES or None)
    #si el fomulario es valido
    if formulario.is_valid():
        #que guarde el formulario
        formulario.save()
        #lo direccione a el html de libros
        return redirect('libros')
    #retorna la vista de crear libro y el los datos de el formulario
    return render(request, "libros/crear.html", {'formulario': formulario})

#vista para editar el libro
def editarLibro(request, id):
    #toma los datos de el libro que contenga la id
    libro = Libro.objects.get(id = id)
    #para tomar los valores de el formulario
    formulario = libroForm(request.POST or None, request.FILES or None, instance=libro)
    #si el formulario es valido y la peticion tambien 
    if formulario.is_valid() and request.POST:
        #que guarde los cambios
        formulario.save()
        #lo redireccione a libros
        return redirect('libros')
    #retorna la vista de editar libro con los datos de el formulario
    return render(request, 'libros/editar.html', {'formulario': formulario})
    
#vista para eliminar el libro
def eliminarLibro(request, id):
    #toma los valores de el libro por id
    libro = Libro.objects.get(id=id)
    #y lo elimina
    libro.delete()
    #y redirecciona a la vista de libros
    return redirect('libros')