from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import producto
from .forms import customUserCreationForm, productoForm
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



  #---------------------------CRUD FARMACIA----------------------------------------------------------------------

def agregar_producto(request):
    data ={
        'form': productoForm()
    }   

    if request.method == 'POST':
        formulario = productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'cesfam/crud_farmacia/agregar.html', data)


def listar_producto(request):
    productos = producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'cesfam/crud_farmacia/listar.html', data)



def editar_producto(request, id):

    
    productos = get_object_or_404(producto, id=id)

    data = {
        'form': productoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = productoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario


    return render(request, 'cesfam/crud_farmacia/editar.html', data)


