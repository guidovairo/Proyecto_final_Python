from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_request, edit_registro

app_name = 'AppUsers'

urlpatterns =[
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='AppAlumno/inicio.html'), name='Logout'),
    path('edit_registro/', edit_registro, name='edit_registro'),
]