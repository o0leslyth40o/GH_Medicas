from django.contrib import admin
from .models import especialidad, genero, medico

# Register your models here.
admin.site.register(especialidad)
admin.site.register(genero)
admin.site.register(medico)