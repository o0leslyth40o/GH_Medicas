from django.urls import path
from .views import home, farmacia, registro

# defini la ruta.
urlpatterns = [
    path('', home, name="home"),
    path('farmacia', farmacia, name="farmacia"),
    path('registro', registro, name="registro"), 
]