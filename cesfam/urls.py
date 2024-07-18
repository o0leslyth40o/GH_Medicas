from django.urls import path
from .views import home, farmacia, agendar, registro, agregar_producto, listar_producto, editar_producto, eliminar_producto, agregar_medico, listar_medico, editar_medico, eliminar_medico

# defini la ruta.
urlpatterns = [
    path('', home, name="home"),
    path('farmacia', farmacia, name="farmacia"),
    path('agendar', agendar, name="agendar"),
    path('registro', registro, name="registro"), 
    path('agregar_producto', agregar_producto, name="agregar_producto"),
    path('listar_producto', listar_producto, name="listar_producto"),
    path('editar_producto/<id>/', editar_producto, name="editar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('agregar_medico', agregar_medico, name="agregar_medico"),
    path('listar_medico', listar_medico, name="listar_medico"),
    path('editar_medico/<id>/', editar_medico, name="editar_medico"),
    path('eliminar_medico/<id>/', eliminar_medico, name="eliminar_medico"),
    
]






