from .forms import UserRegisterForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from HRApp.models import Empleado, Usuario

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequieredHRApp
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


############################## Login ##############################

def LoginHRApp(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect("/HRApp/")
            else:
                return redirect("/HRApp/")
    form = AuthenticationForm()
    return render(request, "hrAppLogin.html", {"form": form})


class StaffRequiredMixin(LoginRequieredHRApp, UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.is_staff

############################## Registro ##############################

def Register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request, f'Usuario {username} creado')
            return redirect("/HWStoreApp/")
    else:
        form = UserRegisterForm()

    return render(request, "registration/register.html", {"form": form})

############################## Pagina principal ##############################

# @login_required


def HRAppInicio(request):

    return render(request, "hrAppIndex.html")

############################## Empleados ##############################

# @login_required


class ListarEmpleados(StaffRequiredMixin, ListView):
    model = Empleado
    template_name = 'listaEmpleados.html'

# @login_required


class BusquedaEmpleado(StaffRequiredMixin, ListView):
    template_name = 'busquedaEmpleado.html'
    model = Empleado

    def get_queryset(self):
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

# Staff Member


class CrearEmpleados(StaffRequiredMixin, CreateView):
    model = Empleado
    template_name = 'crearEmpleados.html'
    fields = ['nombre', 'apellido', 'sexo', 'fecha_nacimiento', 'dni', 'email',
              'direccion', 'telefono', 'salario', 'puesto', 'horario', 'foto_empleado']
    success_url = '/HRApp/ListaEmpleados'

# Staff Member


class ActualizarEmpleados(StaffRequiredMixin, UpdateView):
    model = Empleado
    template_name = 'actualizarEmpleado.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaEmpleados'

# Staff Member


class BorrarEmpleados(StaffRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'borrarEmpleado.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaEmpleados'

############################## Usuarios ##############################

# @login_required


class ListarUsuario(StaffRequiredMixin, ListView):
    model = Usuario
    template_name = 'listaUsuario.html'

# @login_required


class BusquedaUsuario(StaffRequiredMixin, ListView):
    template_name = 'busquedaUsuario.html'
    model = Usuario

    def get_queryset(self):
        query = self.request.GET.get('first_name')
        if query:
            object_list = self.model.objects.filter(first_name__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

# Staff Member


class CrearUsuario(StaffRequiredMixin, CreateView):
    model = Usuario
    template_name = 'crearUsuario.html'
    fields = ['first_name', 'last_name', 'username', 'sexo', 'fecha_nacimiento',
              'dni', 'email', 'direccion', 'telefono', 'foto_usuario']
    success_url = '/HRApp/ListaUsuario'

# Staff Member


class ActualizarUsuario(StaffRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'actualizarUsuario.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaUsuario'

# Staff Member


class BorrarUsuario(StaffRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'borrarUsuario.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaUsuario'
