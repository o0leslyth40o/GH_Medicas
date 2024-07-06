from django.db import models

# Create your models here.
class especialidad(models.Model):
    idEspecialidad = models.IntegerField(primary_key=True, max_length=6, verbose_name='Id Categoria')
    nombre = models.CharField(max_length=50, verbose_name='Especialidad')

    def __str__(self):
        return self.nombre
