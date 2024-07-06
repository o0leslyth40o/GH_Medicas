from django.shortcuts import render
from .models import models
# Cambiar modelo a importar cuando este creado.



# Create your views here.

def home(request):
    return render(request, 'cesfam/home.html')


def farmacia(request):
    # Crear clase modelo para importarla y subir imagenes desde farmacia.
    return render(request, 'cesfam/farmacia.html')

