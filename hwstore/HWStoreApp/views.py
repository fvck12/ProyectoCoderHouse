from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from HWStockApp.models import Productos
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from HWStoreApp.carrito import Carrito


############################## Login ##############################

def LoginStore(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect("HWStoreBienvenida")
            else:
                return redirect("HWStoreBienvenida")
    form = AuthenticationForm()
    return render(request, "HWStoreLogin.html", {"form": form})

class LogoutIfNotStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            logout(request)
            return self.handle_no_permission()
        return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)


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

############################## Productos ##############################


class ComprarProductos(ListView):
    model = Productos
    template_name = 'comprarProductos.html'
    paginate_by = 4
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