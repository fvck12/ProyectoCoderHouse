
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from HRApp.models import Empleado, Cliente

# Create your views here.

def inicio(request):
    
    return render(request, "index.html")

############################## Empleados ##############################

class ListarEmpleados(ListView):
    model = Empleado
    template_name = 'listaEmpleados.html'

class BusquedaEmpleado(ListView):
    template_name = 'busquedaEmpleado.html'
    model = Empleado

    def get_queryset(self):
        print("Ingresando a la funcion busqueda....")
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
            print("Object_list: ", object_list)
        else:
            object_list = self.model.objects.none()
        return object_list

class CrearEmpleados(CreateView):
    model = Empleado
    template_name = 'crearEmpleados.html'
    fields = ['nombre', 'apellido', 'sexo', 'fecha_nacimiento', 'dni', 'email', 'direccion', 'telefono', 'salario', 'puesto', 'horario', 'foto_empleado']
    success_url = '/HRApp/'

class ActualizarEmpleados(UpdateView):
    model = Empleado
    template_name = 'actualizarEmpleado.html'
    fields = ('__all__')
    success_url = '/HRApp/'

class BorrarEmpleados(DeleteView):
    model = Empleado
    template_name = 'borrarEmpleado.html'
    fields = ('__all__')
    success_url = '/HRApp/'

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

############################## Vistas basadas en clases ##############################