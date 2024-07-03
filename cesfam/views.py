from django.shortcuts import render

# Create your views here.

# defini el nombre de la ruta.
def home(request):
    return render(request, 'cesfam/home.html')

def login(request):
    return render(request, 'cesfam/login.html')

def sign_in(request):
    return render(request, 'cesfam/sign_in.html')

def farmacia(request):
    return render(request, 'cesfam/farmacia.html')