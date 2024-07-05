from django.urls import path
from .views import home, login, farmacia, sign_in


# defini la ruta.
urlpatterns = [
    path('', home, name= "home"),
    path('login/', login, name="login"),
    path('farmacia/', farmacia, name="farmacia"),
    path('sign_in/', sign_in, name="sign_in"),
]