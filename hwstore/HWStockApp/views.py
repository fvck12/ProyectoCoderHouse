from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from HWStockApp.models import Productos

# Create your views here.

@login_required
def HWStockAppInicio(request):
    
    return render(request, "HWStockIndex.html")

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
                return render(request, "HWStockIndex.html", {"mensaje": f"Bienvenido {usuario}!"})  
            else:  
                return render(request, "HWStockIndex.html", {"mensaje": "Error, usuario o contraseña son incorrectos!"})
        #return render(request, "hrAppIndex.html", {"mensaje": "Error en el formulario solicitado!"})
    else:
        form = AuthenticationForm()  
    return render (request, "HWStockLogin.html", {"form":form})

def registro(request):    
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "HWStockIndex.html", {"mensaje": "Se ha registrado!"})
    else:
        form = UserCreationForm()
    return render(request, "HWStockRegistro.html", {"form": form})

class LogoutIfNotStaffMixin(AccessMixin):
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_staff:
                logout(request)
                return self.handle_no_permission()
            return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)


############################## Productos ##############################

#Staff Member
class CrearProducto(CreateView):
    model = Productos
    template_name = 'formProducto.html'
    fields = ['nombre', 'stock', 'precio', 'Foto']
    success_url = '/HWStockApp/listaProductos'

@login_required
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

@login_required
class ListarProductos(ListView):
    model = Productos
    template_name = 'listaProductos.html'
    paginate_by: 10

#Staff Member
class BorrarProducto(DeleteView):
    model = Productos
    template_name = 'eliminarProducto.html'
    fields = ('__all__')
    success_url = '/HWStockApp/listaProductos'
    
#Staff Member
class ActualizarProducto(UpdateView):
    model = Productos
    template_name = 'editarProducto.html'
    fields = ('__all__')
    success_url = '/HWStockApp/listaProductos'