from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib import messages

from HRApp.models import Empleado, Cliente
from HRApp.forms import CreateClientForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequieredHRApp
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

    def get_success_url(self):
        # replace url name 'users' on your if need
        return reverse('ListaEmpleados', args=(self.request.user.id,))

    def form_valid(self, form):
        user = self.request.user
        instance, _ = Empleado.objects.get_or_create(user=user)
        instance.rate = form.cleaned_data.get("rate", "")
        instance.availability = form.cleaned_data.get("availability", "")
        instance.save()
        # modify return
        return HttpResponseRedirect(self.get_success_url())

    #success_url = '/HRApp/ListaEmpleados'


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

############################## Clientes ##############################

# @login_required


class ListarClientes(LoginRequieredHRApp, ListView):
    model = Cliente
    template_name = 'listaClientes.html'

# @login_required


class BusquedaCliente(LoginRequieredHRApp, ListView):
    template_name = 'busquedaCliente.html'
    model = Cliente

    def get_queryset(self):
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

# Staff Member


class CrearClientes(LoginRequieredHRApp, CreateView):
    template_name = 'crearCliente.html'
    form_class = CreateClientForm

    def form_valid(self, form):
        c = {'form': form, }
        user_id = form.save(commit=False)
        dni = form.cleaned_data['dni']
        fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        direccion = form.cleaned_data['direccion']
        telefono = form.cleaned_data['telefono']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        if password != repeat_password:
            messages.error(self.request, "Passwords do not Match",
                           extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user_id.set_password(password)
        user_id.save()

        # Create UserProfile model
        Cliente.objects.create(
            user_id=user_id, dni = dni, fecha_nacimiento = fecha_nacimiento, direccion=direccion, telefono=telefono)
        return super(CrearClientes, self).form_valid(form)
    success_url = '/HRApp/ListaClientes'
# Staff Member


class ActualizarClientes(LoginRequieredHRApp, UpdateView):
    model = Cliente
    template_name = 'actualizarCliente.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaClientes'

# Staff Member


class BorrarClientes(LoginRequieredHRApp, DeleteView):
    model = Cliente
    template_name = 'borrarCliente.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaClientes'
