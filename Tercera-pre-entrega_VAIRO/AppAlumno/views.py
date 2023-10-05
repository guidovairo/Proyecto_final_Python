from django.shortcuts import render
from .models import MateriasAprobadas, Cuota, FinalesPrevios


def listar_materias_aprobadas(request):
    materias_aprobadas = MateriasAprobadas.objects.all()
    return render(request, 'listar_materias_aprobadas.html', {'materias_aprobadas': materias_aprobadas})



def listar_cuotas(request):
    cuotas = Cuota.objects.all()
    return render(request, 'listar_cuotas.html', {'cuotas': cuotas})


def listar_finales_previos(request):
    finales_previos = FinalesPrevios.objects.all()
    return render(request, 'listar_finales_previos.html', {'finales_previos': finales_previos})




