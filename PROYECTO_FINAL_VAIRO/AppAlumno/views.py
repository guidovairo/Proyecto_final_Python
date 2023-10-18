from django.shortcuts import render
from .models import MateriasAprobadas, Cuota, FinalesPrevios
from AppAlumno.forms import CuotaFormulario
from AppUsers.models import Avatar



from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin






#VISTA DE INICIO

@login_required(login_url="AppUsers:Login")
def vista_inicio(request):
    imagen = Avatar.objects.filter(user=request.user.id).first()
    url_imagen = imagen.imagen.url if imagen and imagen.imagen else None
    return render(request, 'AppAlumno/inicio.html', {'url': url_imagen})




#VISTAS BASADAS EN CLASES PARA EL MODELO DE CUOTAS

class cuotasListView(LoginRequiredMixin, ListView):
    model = Cuota
    template_name = "AppAlumno/lista.html"
    login_url = "AppUsers:Login"


class cuotasDetalle(LoginRequiredMixin, DetailView):
    model = Cuota
    template_name = "AppAlumno/cuotas_detalle.html"
    login_url = "AppUsers:Login"


class cuotasCreateView(LoginRequiredMixin, CreateView):
    model = Cuota
    template_name = "AppAlumno/cuotasFormulario.html"
    success_url = reverse_lazy("lista_cuotas")
    fields = ["debe_cuotas", "importe_a_pagar"]
    login_url = "AppUsers:Login"


class cuotasUpdateView(LoginRequiredMixin, UpdateView):
    model = Cuota
    template_name = "AppAlumno/editar_cuotas.html"
    success_url = reverse_lazy("lista_cuotas")
    fields = ["debe_cuotas", "importe_a_pagar"]
    login_url = "AppUsers:Login"


class cuotasDeleteView(LoginRequiredMixin, DeleteView):
    model = Cuota
    success_url = reverse_lazy("lista_cuotas")
    template_name = "AppAlumno/confirm_delete_cuotas.html"
    login_url = "AppUsers:Login"





#VISTAS BASADAS EN CLASES PARA EL MODELO DE MATERIAS APROBADAS

class materiasListView(LoginRequiredMixin, ListView):
    model = MateriasAprobadas
    template_name = "AppAlumno/lista_materias.html"
    login_url = "AppUsers:Login"


class materiasDetalle(LoginRequiredMixin, DetailView):
    model = MateriasAprobadas
    template_name = "AppAlumno/materias_detalle.html"
    login_url = "AppUsers:Login"


class materiasCreateView(LoginRequiredMixin, CreateView):
    model = MateriasAprobadas
    template_name = "AppAlumno/materiasFormulario.html"
    success_url = reverse_lazy("lista_materias")
    fields = ["materia", "Nota_primer_parcial", "Nota_segundo_parcial", "Nota_del_final"]
    login_url = "AppUsers:Login"


class materiasUpdateView(LoginRequiredMixin, UpdateView):
    model = MateriasAprobadas
    template_name = "AppAlumno/editar_materias.html"
    success_url = reverse_lazy("lista_materias")
    fields = ["materia", "Nota_primer_parcial", "Nota_segundo_parcial", "Nota_del_final"]
    login_url = "AppUsers:Login"


class materiasDeleteView(LoginRequiredMixin, DeleteView):
    model = MateriasAprobadas
    success_url = reverse_lazy("lista_materias")
    template_name = "AppAlumno/confirm_delete_materias.html"
    login_url = "AppUsers:Login"






#VISTAS BASADAS EN CLASES PARA EL MODELO DE FINALES PREVIOS

class finalesListView(LoginRequiredMixin, ListView):
    model = FinalesPrevios
    template_name = "AppAlumno/lista_finales.html"
    login_url = "AppUsers:Login"


class finalesDetalle(DetailView):
    model = FinalesPrevios
    template_name = "AppAlumno/finales_detalle.html"
    login_url = "AppUsers:Login"


class finalesCreateView(LoginRequiredMixin, CreateView):
    model = FinalesPrevios
    template_name = "AppAlumno/finalesFormulario.html"
    success_url = reverse_lazy("lista_finales")
    fields = ["debe_final_de"]
    login_url = "AppUsers:Login"


class finalesUpdateView(LoginRequiredMixin, UpdateView):
    model = FinalesPrevios
    template_name = "AppAlumno/editar_finales.html"
    success_url = reverse_lazy("lista_finales")
    fields = ["debe_final_de"]
    login_url = "AppUsers:Login"


class finalesDeleteView(LoginRequiredMixin, DeleteView):
    model = FinalesPrevios
    success_url = reverse_lazy("lista_finales")
    template_name = "AppAlumno/confirm_delete_finales.html"
    login_url = "AppUsers:Login"



#ACERCA DE MI
def acerca_de_mi(request):
    return render(request, 'AppAlumno/about.html')































    

    







