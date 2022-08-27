from django.urls import path
from HWStoreApp.views import HWStoreInicio, LoginStore, HWStoreAbout, HWStoreBienvenida
from django.contrib.auth.views import LogoutView
from HWStoreApp.views import ListarProductos, BusquedaProducto

urlpatterns = [
    path('', HWStoreInicio, name="HWStoreInicio"),
    path('HWStoreAbout/', HWStoreAbout, name="HWStoreAbout"),
    path('LoginStore/', LoginStore, name="LoginStore"),
    path('LogoutStore/', LogoutView.as_view(template_name='HWStoreLogout.html'),
         name="LogoutStore"),
    path('HWStoreBienvenida/', HWStoreBienvenida, name="HWStoreBienvenida"),
    
    path('ListarProductos/', ListarProductos.as_view(), name="ListarProductos"),
    path('BusquedaProducto/', BusquedaProducto.as_view(), name="BusquedaProducto"),
]
