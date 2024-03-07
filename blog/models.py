from django.db import models

class contenido(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, null=True)
    Titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="imagenes", null=True)
    descripcion = models.TextField(max_length=1000, null=True, default="Sin Comentario.")
    fechaCreada = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellido
    

