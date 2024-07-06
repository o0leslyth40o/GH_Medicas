from django.db import models

# Create your models here.
class especialidad(models.Model):
    idEspecialidad = models.IntegerField(primary_key=True, max_length=6, verbose_name='Id Categoria')
    nombre = models.CharField(max_length=50, verbose_name='Especialidad')

    def __str__(self):
        return self.nombre

class genero(models.Model):
    genero = models.CharField(db_column='genero', max_length=20, blank=False, null=False)

    def __str__(self):
        return self.genero

class medico(models.model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    appaterno = models.CharField(max_length=30, verbose_name='Apellido Paterno')
    apmaterno = models.CharField(max_length=30, verbose_name='Apellido Materno')
    especialidad = models.ForeignKey(especialidad, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre