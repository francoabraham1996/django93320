from django.db import models

# Create your models here.
class Pintura(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_de_creacion = models.DateField(auto_now_add=True)
    nro_pintura = models.IntegerField(unique=True)


    def __str__(self):
        return f'Pintura "{self.nombre}" del autor "{self.autor}"'
    