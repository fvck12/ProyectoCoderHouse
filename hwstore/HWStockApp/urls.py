from django.urls import path
from HWStockApp.views import ListarProductos, BusquedasProducto, CrearProducto, ActualizarProductos, BorrarProductos
from HWStockApp.views import HWStockInicio, LoginStock
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HWStockInicio, name="HWStockInicio"),
    path('LoginStock/', LoginStock, name="LoginStock"),
    path('LogoutStock/', LogoutView.as_view(template_name='HWStockLogout.html'),
         name="LogoutStock"),

    path('ListarProductos/', ListarProductos.as_view(), name="ListarProductos"),
    path('CrearProducto/', CrearProducto.as_view(), name="CrearProducto"),
    path('ActualizarProductos/<int:pk>',
         ActualizarProductos.as_view(), name="ActualizarProductos"),
    path('BorrarProductos/<int:pk>',
         BorrarProductos.as_view(), name="BorrarProductos"),
    path('BusquedasProducto/', BusquedasProducto.as_view(), name="BusquedasProducto"),
]
