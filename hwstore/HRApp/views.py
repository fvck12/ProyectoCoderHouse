from .forms import UserRegisterForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from HRApp.models import Empleado, Usuario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequieredHRApp, AccessMixin
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


class LogoutIfNotStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            logout(request)
            return self.handle_no_permission()
        return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)

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


class ListarEmpleados(LoginRequieredHRApp, ListView):
    model = Empleado
    template_name = 'listaEmpleados.html'

# @login_required


class BusquedaEmpleado(LoginRequieredHRApp, ListView):
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


class CrearEmpleados(LoginRequieredHRApp, CreateView):
    model = Empleado
    template_name = 'crearEmpleados.html'
    fields = ['nombre', 'apellido', 'sexo', 'fecha_nacimiento', 'dni', 'email',
              'direccion', 'telefono', 'salario', 'puesto', 'horario', 'foto_empleado']
    success_url = '/HRApp/ListaEmpleados'

# Staff Member


class ActualizarEmpleados(LoginRequieredHRApp, UpdateView):
    model = Empleado
    template_name = 'actualizarEmpleado.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaEmpleados'

# Staff Member


class BorrarEmpleados(LoginRequieredHRApp, DeleteView):
    model = Empleado
    template_name = 'borrarEmpleado.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaEmpleados'

############################## Usuarios ##############################

# @login_required


class ListarUsuario(LoginRequieredHRApp, ListView):
    model = Usuario
    template_name = 'listaUsuario.html'

# @login_required


class BusquedaUsuario(LoginRequieredHRApp, ListView):
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


class CrearUsuario(LoginRequieredHRApp, CreateView):
    model = Usuario
    template_name = 'crearUsuario.html'
    fields = ['first_name', 'last_name', 'username', 'sexo', 'fecha_nacimiento',
              'dni', 'email', 'direccion', 'telefono', 'foto_usuario']
    success_url = '/HRApp/ListaUsuario'

# Staff Member


class ActualizarUsuario(LoginRequieredHRApp, UpdateView):
    model = Usuario
    template_name = 'actualizarUsuario.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaUsuario'

# Staff Member


class BorrarUsuario(LoginRequieredHRApp, DeleteView):
    model = Usuario
    template_name = 'borrarUsuario.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaUsuario'
