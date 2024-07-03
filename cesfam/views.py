from django.shortcuts import render

# Create your views here.

# defini el nombre de la ruta.
def home(request):
    return render(request, 'cesfam/home.html')

