from django.urls import path
from AppRegister.views import register

urlpatterns =[
    path('register/', register, name='Register'),
]