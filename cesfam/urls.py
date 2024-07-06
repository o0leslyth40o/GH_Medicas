from django.urls import path
from .views import home, farmacia

# defini la ruta.
urlpatterns = [
    path('', home, name="home"),
    path('farmacia', farmacia, name="farmacia"),
]