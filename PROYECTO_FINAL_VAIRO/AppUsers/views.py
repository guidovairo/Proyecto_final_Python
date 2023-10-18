from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Avatar

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from AppUsers.forms import UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



# Create your views here.

#LOGIN
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            nombre_usuario = authenticate(username=usuario, password=clave)

            if nombre_usuario is not None:
                login(request, nombre_usuario)

                return redirect('vista_inicio')

            else:
                form = AuthenticationForm()
                return render(request, "AppUsers/login.html", {"mensaje": f"Error, datos incorrectos", "form": form})

        else:
            return render(request, "AppUsers/login.html", {"mensaje": f"Error, formulario inválido"})

    form = AuthenticationForm()
    return render(request, "AppUsers/login.html", {"form": form})





#EDITAR PERFIL
def edit_registro(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': usuario.first_name,
                    'email': usuario.email 
                }
                miFormulario = UserEditForm(initial=datos)

            else:
                usuario.email = informacion['email']
                usuario.set_password(informacion['password1'])
                usuario.last_name = informacion['last_name']  
                usuario.first_name = informacion['first_name']  
                usuario.save()

                try:
                    avatar = Avatar.objects.get(user=usuario)
                except Avatar.DoesNotExist:
                    avatar = Avatar(user=usuario, imagen=request.FILES.get("imagen"))
                    avatar.save()
                else:
                    avatar.imagen = request.FILES.get("imagen")
                    avatar.save()

                
                user = authenticate(username=usuario.username, password=informacion['password1'])
                login(request, user)

                messages.success(request, 'Perfil actualizado correctamente.')

                return redirect('vista_inicio')

    else:
        datos = {'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name}
        miFormulario = UserEditForm(initial=datos)

    return render(request, "AppUsers/edit_registro.html", {"mi_form": miFormulario, "usuario": usuario})





