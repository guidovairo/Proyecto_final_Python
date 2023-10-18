from django.shortcuts import render
from AppRegister.forms import UserRegisterForm


# Create your views here.

#REGISTER

def register(request):
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppAlumno/inicio.html", {"mensaje":f"{username}, Usuario creado"})
        

    else:
        form = UserRegisterForm()

    return render(request, "AppRegister/register.html", {"form": form})
