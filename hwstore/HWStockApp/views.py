from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from HWStockApp.models import Productos

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin

############################## Login ##############################

def LoginStock(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect("/HWStockApp/")
            else:
                return redirect("/HWStockApp/")
    form = AuthenticationForm()
    return render(request, "HWStockLogin.html", {"form": form})


class LogoutIfNotStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            logout(request)
            return self.handle_no_permission()
        return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)

############################## Pagina principal ##############################

def HWStockInicio(request):

    return render(request, "HWStockIndex.html")

############################## Productos ##############################


class ListarProductos(LoginRequiredMixin, LogoutIfNotStaffMixin, ListView):
    model = Productos
    template_name = 'listaProductos.html'
    fields = ('__all__')
    paginate_by: 10


class BusquedasProducto(LoginRequiredMixin, LogoutIfNotStaffMixin, ListView):
    template_name = 'HWStockBuscarProducto.html'
    model = Productos

    def get_queryset(self):
        query = self.request.GET.get('nombre')
        if query:
            object_list = self.model.objects.filter(nombre__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class CrearProducto(LoginRequiredMixin, LogoutIfNotStaffMixin, CreateView):
    model = Productos
    template_name = 'crearProductos.html'
    fields = ('__all__')
    success_url = '/HWStockApp/ListarProductos/'



class ActualizarProductos(LoginRequiredMixin, LogoutIfNotStaffMixin, UpdateView):
    model = Productos
    template_name = 'actualizarProducto.html'
    fields = ('__all__')
    success_url = '/HWStockApp/ListarProductos/'



class BorrarProductos(LoginRequiredMixin, LogoutIfNotStaffMixin, DeleteView):
    model = Productos
    template_name = 'borrarProducto.html'
    fields = ('__all__')
    success_url = '/HWStockApp/ListarProductos/'
