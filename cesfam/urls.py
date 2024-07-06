from django.urls import path
from .views import home, farmacia, login


# defini la ruta.
urlpatterns = [
    path('', home, name="home"),
    path('farmacia', farmacia, name="farmacia"),
    path('login', login, name="login"),
]