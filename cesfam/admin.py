from django.contrib import admin
from .models import especialidad, genero, medico, paciente, ficha, sector, agenda, atencion, producto

class productoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "stock"]
    list_editable = ["stock"]

class medicoAdmin(admin.ModelAdmin):
    list_display = ["rut","nombre", "appaterno", "especialidad", "imagen"]
    search_fields = ["nombre"]
    list_filter = ["especialidad"]

# Register your models here.
admin.site.register(especialidad)
admin.site.register(genero)
admin.site.register(medico, medicoAdmin)
admin.site.register(paciente)
admin.site.register(ficha)
admin.site.register(sector)
admin.site.register(agenda)
admin.site.register(atencion)
admin.site.register(producto, productoAdmin)