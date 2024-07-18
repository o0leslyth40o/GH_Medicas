from django import forms
from .models import producto, medico
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class customUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]


class productoForm(forms.ModelForm):

    class Meta:
        model = producto
        fields = '__all__'

class medicoForm(forms.ModelForm):

    class Meta:
        model = medico
        fields = '__all__'
