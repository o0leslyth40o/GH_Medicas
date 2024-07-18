from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import producto, medico, agenda
from .forms import customUserCreationForm, productoForm, medicoForm, agendaForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
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

def agendar(request):
    agendas = agenda.objects.all()
    data = {
        'agendas': agendas
    }
    if request.method == 'POST':
        formulario = agendaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Su hora ha sido agendada correctamente"
        else:
            data["form"] = formulario

    return render(request, 'cesfam/agendar.html', data)


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

@permission_required('cesfam.add_producto')
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


@permission_required('cesfam.view_producto')
def listar_producto(request):
    productos = producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'cesfam/crud_farmacia/listar.html', data)


@permission_required('cesfam.change_producto')
def editar_producto(request, id):
    productos = get_object_or_404(producto, id=id)
    data = {
        'form': productoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = productoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario
    return render(request, 'cesfam/crud_farmacia/editar.html', data)

@permission_required('cesfam.delete_producto')
def eliminar_producto(request, id):
    productos = get_object_or_404(producto, id=id)
    productos.delete()
    return redirect(to="listar_producto")



#---------------------------CRUD MEDICO----------------------------------------------------------------------
@permission_required('cesfam.add_medico')
def agregar_medico(request):
    data ={
        'form': medicoForm()
    }   

    if request.method == 'POST':
        formulario = medicoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'cesfam/crud_medico/agregar.html', data)

@permission_required('cesfam.view_medico')
def listar_medico(request):

    medicos = medico.objects.all()
    data = {
        'medicos': medicos
    }
    return render(request, 'cesfam/crud_medico/listar.html', data)

@permission_required('cesfam.change_medico')
def editar_medico(request, id):

    medicos = get_object_or_404(medico, id=id)
    data = {
        'form': medicoForm(instance=medicos)
    }

    if request.method == 'POST':
        formulario = medicoForm(data=request.POST, instance=medicos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
            return redirect(to="listar_medico")
        else:
            data["form"] = formulario
    return render(request, 'cesfam/crud_medico/editar.html', data)

@permission_required('cesfam.delete_medico')
def eliminar_medico(request, id):
    medicos = get_object_or_404(medico, id=id)
    medicos.delete()
    return redirect(to="listar_medico")










