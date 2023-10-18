from django.urls import path
from .views import vista_inicio, cuotasListView, cuotasDeleteView, cuotasCreateView, cuotasUpdateView, cuotasDetalle, materiasCreateView, materiasDeleteView, materiasDetalle, materiasListView, materiasUpdateView, finalesListView, finalesCreateView, finalesDeleteView, finalesDetalle, finalesUpdateView, acerca_de_mi




urlpatterns =[
    path('inicio/', vista_inicio, name='vista_inicio'),



    path('lista_cuotas/', cuotasListView.as_view(), name='lista_cuotas'),
    path('detalle_cuotas/<int:pk>/', cuotasDetalle.as_view(), name='detalle_cuotas'),
    path('crear_cuotas/', cuotasCreateView.as_view(), name='crear_cuotas'),
    path('editar_cuotas/<int:pk>/', cuotasUpdateView.as_view(), name='editar_cuotas'),
    path('eliminar_cuotas/<int:pk>/', cuotasDeleteView.as_view(), name='eliminar_cuotas'),




    path('lista_materias/', materiasListView.as_view(), name='lista_materias'),
    path('detalle_materias/<int:pk>/', materiasDetalle.as_view(), name='detalle_materias'),
    path('crear_materias/', materiasCreateView.as_view(), name='crear_materias'),
    path('editar_materias/<int:pk>/', materiasUpdateView.as_view(), name='editar_materias'),
    path('eliminar_materias/<int:pk>/', materiasDeleteView.as_view(), name='eliminar_materias'),





    path('lista_finales/', finalesListView.as_view(), name='lista_finales'),
    path('detalle_finales/<int:pk>/', finalesDetalle.as_view(), name='detalle_finales'),
    path('crear_finales/', finalesCreateView.as_view(), name='crear_finales'),
    path('editar_finales/<int:pk>/', finalesUpdateView.as_view(), name='editar_finales'),
    path('eliminar_finales/<int:pk>/', finalesDeleteView.as_view(), name='eliminar_finales'),



    
    
    
    

    path('about/', acerca_de_mi, name='about')


]




