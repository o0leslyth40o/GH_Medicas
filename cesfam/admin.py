from django.contrib import admin
from .models import especialidad, genero, medico, paciente, ficha

# Register your models here.
admin.site.register(especialidad)
admin.site.register(genero)
admin.site.register(medico)
admin.site.register(paciente)
admin.site.register(ficha)