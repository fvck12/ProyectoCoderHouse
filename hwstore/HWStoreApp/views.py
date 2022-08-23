from django.shortcuts import render

from HRApp.models import Empleado, Cliente
from HWStockApp.models import Productos

#Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "HWStoreApp/", {"mensaje": f"Bienvenido{usuario}"})
            else:
                return render(request, "HWStoreApp/", {"mensaje":"Error, datos erroneos"})
        else:
                return render(request, "HWStoreApp/", {"mensaje": "Erorr, formulario erroneo"})
    form = AuthenticationForm()
    return render (request, "login.html", {"form":form})

def registro(request):    
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "HWStoreApp/", {"mensaje":"Usuario creado"})
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})

# Create your views here.
def inicio(request):
    
    return render (request, "index.html")

def access_denied(request):

    return render (request, "AccessDenied.html")