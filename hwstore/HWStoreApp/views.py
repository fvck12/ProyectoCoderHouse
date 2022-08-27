from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from HWStockApp.models import Productos
from django.views.generic import ListView, DeleteView, CreateView, UpdateView


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

    return render(request, "HWStoreIndex.html")

def HWStoreAbout(request):
    
    return render(request, "HWStoreAbout.html")

def HWStoreBienvenida(request):
    
    return render(request, "HWStoreIndex.html", {"mensaje": "Bienvenido!"})

############################## Productos ##############################


class ListarProductos(ListView):
    model = Productos
    template_name = 'listaProductos.html'
    fields = ('__all__')
    paginate_by: 9


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

