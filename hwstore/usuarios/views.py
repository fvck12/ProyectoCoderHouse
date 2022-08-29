from curses.ascii import US
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = "/HRApp/ListaEmpleados"