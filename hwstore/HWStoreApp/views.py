from django.shortcuts import render, redirect
from HWStockApp.models import Productos
from django.views.generic import ListView
from HWStoreApp.carrito import Carrito


############################## Pagina principal ##############################


def HWStoreInicio(request):
    productos= Productos.objects.all()
    return render(request, "HWStoreIndex.html", {"productos":productos})

def HWStoreAbout(request):
    
    return render(request, "HWStoreAbout.html")

def HWStoreBienvenida(request):
    
    return render(request, "HWStoreIndex.html", {"mensaje": "Bienvenido!"})

def HWStoreCarrito(request):
    
    return render(request, "HWStoreCarrito.html")

def NoWebPage(request):
    
    return render(request, "NoWebPage.html")

############################## Productos ##############################


class ComprarProductos(ListView):
    model = Productos
    template_name = 'comprarProductos.html'
    paginate_by = 8
    fields = ('__all__')
   


class BusquedaProducto(ListView):
    paginate_by = 4 
    template_name = 'busquedaProducto.html'
    model = Productos 
      

    def get_queryset(self):
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list   

############################## Carrito ##############################

def agregar_productos(request, productos_id):
    carrito = Carrito(request)
    productos= Productos.objects.get(id=productos_id)
    carrito.agregar(productos)
    return redirect("ComprarProductos")

def eliminar_productos(request, productos_id):
    carrito = Carrito(request)
    productos = Productos.objects.get(id=productos_id)
    carrito.eliminar(productos)
    return redirect("ComprarProductos")

def restar_productos(request, productos_id):
    carrito = Carrito(request)
    productos = Productos.objects.get(id=productos_id)
    carrito.restar(productos)
    return redirect("ComprarProductos")

def eliminar_carrito(request):
    carrito= Carrito(request)
    carrito.limpiar()
    return redirect("ComprarProductos")