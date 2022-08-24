
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from HRApp.models import Empleado, Cliente

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequieredHRApp, AccessMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

############################## Login ##############################

def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():    
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")    
            user = authenticate(username=usuario, password=contra)    
            if user is not None:   
                login(request, user)   
                return render(request, "hrAppIndex.html", {"mensaje": f"Bienvenido {usuario}!"})  
            else:  
                return render(request, "hrAppIndex.html", {"mensaje": "Error, usuario o contraseña son incorrectos!"})
        #return render(request, "hrAppIndex.html", {"mensaje": "Error en el formulario solicitado!"})
    else:
        form = AuthenticationForm()  
    return render (request, "hrAppLogin.html", {"form":form})

class LogoutIfNotStaffMixin(AccessMixin):
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_staff:
                logout(request)
                return self.handle_no_permission()
            return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)

############################## Pagina principal ##############################

#@login_required
def hrAppInicio(request):
    
    return render(request, "hrAppIndex.html")

############################## Empleados ##############################

#@login_required
class ListarEmpleados(LoginRequieredHRApp, ListView):
    model = Empleado
    template_name = 'listaEmpleados.html'

#@login_required
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

#Staff Member
class CrearEmpleados(LoginRequieredHRApp, CreateView):
    model = Empleado
    template_name = 'crearEmpleados.html'
    fields = ['nombre', 'apellido', 'sexo', 'fecha_nacimiento', 'dni', 'email', 'direccion', 'telefono', 'salario', 'puesto', 'horario', 'foto_empleado']
    success_url = '/HRApp/ListaEmpleados'

#Staff Member
class ActualizarEmpleados(LoginRequieredHRApp, UpdateView):
    model = Empleado
    template_name = 'actualizarEmpleado.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaEmpleados'

#Staff Member
class BorrarEmpleados(LoginRequieredHRApp, DeleteView):
    model = Empleado
    template_name = 'borrarEmpleado.html'
    fields = ('__all__')
    success_url = '/HRApp/ListaEmpleados'

############################## Clientes ##############################

class CrearCliente(CreateView):
    model = Cliente
    template_name = 'formClientes.html'
    fields = ['nombre', 'apellido', 'nombre_usuario', 'sexo', 'fecha_nacimiento', 'dni', 'email', 'direccion', 'telefono', 'foto_cliente']
    success_url = '/webapp/listaClientes' 

class BusquedaCliente(ListView):
    template_name = 'busquedaCliente.html'
    model = Cliente

    def get_queryset(self):
        print("Ingresando a la funcion busqueda....")
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
            print("Object_list: ", object_list)
        else:
            object_list = self.model.objects.none()
        return object_list

class ListarClientes(ListView):
    model = Cliente
    template_name = 'listaClientes.html'

class BorrarCliente(DeleteView):
    model = Cliente
    template_name = 'eliminarCliente.html'
    fields = ('__all__')
    success_url = '/webapp/listaClientes'

class ActualizarCliente(UpdateView):
    model = Cliente
    template_name = 'editarCliente.html'
    fields = ('__all__')
    success_url = '/webapp/listaClientes'