from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from HWStockApp.models import Productos

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
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

############################## Pagina principal ##############################
#@login_required
def HWStockAppInicio(request):
    
    return render(request, "HWStockIndex.html")

############################## Productos ##############################

#@login_required
class ListarProductos(ListView):
    model = Productos
    template_name = 'listaProductos.html'
    fields = ('__all__')
    paginate_by: 10

#@login_required
class BusquedaProducto(ListView):
    template_name = 'busquedaProducto.html'
    model = Productos

    def get_queryset(self):
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

#Staff Member
class CrearProducto(LoginRequiredMixin, CreateView):
    model = Productos
    template_name = 'crearProductos.html'
    fields = ['nombre', 'stock', 'precio', 'Foto']
    success_url = '/HWStockApp/ListarProductos/'

#Staff Member
class ActualizarProductos(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = 'actualizarProducto.html'
    fields = ('__all__')
    success_url = '/HWStockApp/ListarProductos/'

#Staff Member
class BorrarProductos(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = 'borrarProducto.html'
    fields = ('__all__')
    success_url = '/HWStockApp/ListarProductos/'
