from django.db import models
'''modelo para hacer la sql'''
'''usamos python manage.py migrate'''
'''luego python manage.py makemigrations'''
'''el verbose_name se usa para nombras las columnas'''
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 100, verbose_name ='Titulo')
    imagen = models.ImageField(upload_to = 'imagenes/', verbose_name='Imagen', null= True)
    descripcion = models.TextField(verbose_name = 'Descripcion', null = True)
    def __str__(self):
        fila = "titulo: " + self.titulo + "-" + "Descripcion " + self.descripcion
        return fila
    def delete(self, using=None , keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
