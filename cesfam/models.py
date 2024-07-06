from django.db import models

# Create your models here.
class especialidad(models.Model):
    idEspecialidad = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombre = models.CharField(max_length=50, verbose_name='Especialidad')

    def __str__(self):
        return self.nombre

class genero(models.Model):
    genero = models.CharField(db_column='genero', max_length=20, blank=False, null=False)

    def __str__(self):
        return self.genero

class medico(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    appaterno = models.CharField(max_length=30, verbose_name='Apellido Paterno')
    apmaterno = models.CharField(max_length=30, verbose_name='Apellido Materno')
    especialidad = models.ForeignKey('especialidad', on_delete=models.CASCADE)
    genero = models.ForeignKey('genero', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre +" "+ self.appaterno +" "+ self.apmaterno
    
    
class paciente(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    appaterno = models.CharField(max_length=30, verbose_name='Apellido Paterno')
    apmaterno = models.CharField(max_length=30, verbose_name='Apellido Materno')
    nFicha = models.ForeignKey('ficha', on_delete=models.CASCADE)
    edad = models.IntegerField(verbose_name='Edad')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    genero = models.ForeignKey('genero', on_delete=models.CASCADE, db_column='genero')

    def __str__(self):
        return self.nombre +" "+ self.appaterno +" "+ self.apmaterno
   

class ficha(models.Model):
    nFicha = models.IntegerField(db_column='nFicha', primary_key=True, verbose_name='Numero de Ficha')
    direccion = models.ForeignKey('paciente', on_delete=models.CASCADE)
    rut = models.ForeignKey('paciente', on_delete=models.PROTECT, verbose_name='Rut')
    sector = models.CharField(max_length=10)

    def __str__(self):
        return self.nFicha


    