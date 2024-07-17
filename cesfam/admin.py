from django.contrib import admin
from .models import especialidad, genero, medico, paciente, ficha, sector, agenda, atencion, producto


# Register your models here.
admin.site.register(especialidad)
admin.site.register(genero)
admin.site.register(medico)
admin.site.register(paciente)
admin.site.register(ficha)
admin.site.register(sector)
admin.site.register(agenda)
admin.site.register(atencion)
admin.site.register(producto)