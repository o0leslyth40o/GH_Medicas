from django.urls import path
from .views import home, farmacia, registro, agregar_producto

# defini la ruta.
urlpatterns = [
    path('', home, name="home"),
    path('farmacia', farmacia, name="farmacia"),
    path('registro', registro, name="registro"), 
    path('agregar_producto', agregar_producto, name="agregar_producto"),
]






