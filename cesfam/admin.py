from django.contrib import admin
from .models import medico, especialidad, paciente

# Register your models here.
admin.site.register(medico)
admin.site.register(especialidad)
admin.site.register(paciente)