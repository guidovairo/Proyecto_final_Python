from django.shortcuts import render
from .models import MateriasAprobadas, Cuota, FinalesPrevios
from AppAlumno.forms import CuotaFormulario
from django.http import HttpResponse


def vista_inicio(request):
    return render(request, 'AppAlumno/inicio.html')


def materias_aprobadas(request):
    materias_aprobadas = MateriasAprobadas.objects.all()
    return render(request, 'AppAlumno/materias_aprobadas.html', {'materias_aprobadas': materias_aprobadas})



def cuotas(request):
    cuotas = Cuota.objects.all()
    return render(request, 'AppAlumno/cuotas.html', {'cuotas': cuotas})


def finales_previos(request):
    finales_previos = FinalesPrevios.objects.all()
    return render(request, 'AppAlumno/finales_previos.html', {'finales_previos': finales_previos})




def cuotasFormu(request):
    if request.method == "POST":
        cuota_form = CuotaFormulario(request.POST)

        if cuota_form.is_valid():
            informacion = cuota_form.cleaned_data
            cuota = Cuota(debe_cuotas=informacion["cuota"])  

            cuota.save()
            return render(request, "AppAlumno/inicio.html")
    else:
        cuota_form = CuotaFormulario()

    return render(request, "AppAlumno/cuotasFormulario.html", {"cuota_form": cuota_form})



def buscar(request):
    if request.method == "POST":
        cuota_form = CuotaFormulario(request.POST)

        if cuota_form.is_valid():
            informacion = cuota_form.cleaned_data
            
            cuotas = Cuota.objects.filter(debe_cuotas__icontains=informacion["cuota"])
            
            
            return render(request, "AppAlumno/busquedaCuota.html", {"cuotas": cuotas})
    else:
        cuota_form = CuotaFormulario()

    return render(request, "AppAlumno/cuotasFormulario.html", {"cuota_form": cuota_form})



    

    







