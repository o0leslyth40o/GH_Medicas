from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import producto
from .forms import customUserCreationForm
from django.contrib.auth import authenticate, login
# Cambiar modelo a importar cuando este creado.



# Create your views here.

def home(request):
    return render(request, 'cesfam/home.html')


def farmacia(request):
    productos = producto.objects.all()
    data = {
        'productos': productos
    }
    # Crear clase modelo para importarla y subir imagenes desde farmacia.
    return render(request, 'cesfam/farmacia.html', data)

def registro(request):
    data = {
        'form': customUserCreationForm()
    }

    if request.method == 'POST':
        formulario = customUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")

        data["form"] = formulario
    return render(request, 'registration/registro.html', data)