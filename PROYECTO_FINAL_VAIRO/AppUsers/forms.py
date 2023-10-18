from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




#EDITAR PERFIL
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email: ")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name', 'imagen']