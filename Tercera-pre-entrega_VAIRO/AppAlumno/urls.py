from django.urls import path
from .views import vista_inicio, cuotas, materias_aprobadas, finales_previos, cuotasFormu, buscar

urlpatterns = [
    path('inicio/', vista_inicio, name='vista_inicio'),
    path('cuotas/', cuotas, name='cuotas'),
    path('ma/', materias_aprobadas, name='materias_aprobadas'),
    path('fp/', finales_previos, name='finales_previos'),
    path('cuotasformul/', cuotasFormu, name='cuotas_formul'),
    path('buscar/', buscar, name='buscar'),
    



]