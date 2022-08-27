from django.urls import path
from HWStoreApp.views import HWStoreInicio, LoginStore, HWStoreAbout, HWStoreBienvenida
from django.contrib.auth.views import LogoutView
from HWStoreApp.views import ListarProductos, BusquedaProducto
from HWStoreApp.views import agregar_productos, eliminar_productos, restar_productos, eliminar_carrito

urlpatterns = [
    path('', HWStoreInicio, name="HWStoreInicio"),
    path('HWStoreAbout/', HWStoreAbout, name="HWStoreAbout"),
    path('LoginStore/', LoginStore, name="LoginStore"),
    path('LogoutStore/', LogoutView.as_view(template_name='HWStoreLogout.html'),
         name="LogoutStore"),
    path('HWStoreBienvenida/', HWStoreBienvenida, name="HWStoreBienvenida"),

    path('ListarProductos/', ListarProductos.as_view(), name="ListarProductos"),
    path('BusquedaProducto/', BusquedaProducto.as_view(), name="BusquedaProducto"),

    path('agregar/<int:productos_id>/', agregar_productos, name="Add"),
    path('eliminar/<int:productos_id>/', eliminar_productos, name="Del"),
    path('restar/<int:productos_id>/', restar_productos, name="Sub"),
    path('limpiar/', eliminar_carrito, name="CLS"),
]
