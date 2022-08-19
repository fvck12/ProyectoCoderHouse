from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from HWStockApp.models import Productos

# Create your views here.


def HWStockAppInicio(request):
    
    return render(request, "HWStockIndex.html")

############################## Productos ##############################
class CrearProducto(CreateView):
    model = Productos
    template_name = 'formProducto.html'
    fields = ['nombre', 'stock', 'precio', 'Foto']
    success_url = '/HWStockApp/listaProductos'


class BusquedaProducto(ListView):
    template_name = 'busquedaProductos.html'
    model = Productos

    def get_queryset(self):
        print("Ingresando a la funcion busqueda....")
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
            print("Object_list: ", object_list)
        else:
            object_list = self.model.objects.none()
        return object_list


class ListarProductos(ListView):
    model = Productos
    template_name = 'listaProductos.html'
    paginate_by: 10


class BorrarProducto(DeleteView):
    model = Productos
    template_name = 'eliminarProducto.html'
    fields = ('__all__')
    success_url = '/HWStockApp/listaProductos'


class ActualizarProducto(UpdateView):
    model = Productos
    template_name = 'editarProducto.html'
    fields = ('__all__')
    success_url = '/HWStockApp/listaProductos'

