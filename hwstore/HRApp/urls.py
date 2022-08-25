from django.urls import path
from HRApp.views import ListarEmpleados, BusquedaEmpleado, CrearEmpleados, ActualizarEmpleados, BorrarEmpleados
from HRApp.views import ListarClientes, BusquedaCliente, CrearClientes, ActualizarClientes, BorrarClientes
from HRApp.views import HRAppInicio, LoginHRApp
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HRAppInicio, name="HRAppInicio"),
    path('HRLogin/', LoginHRApp, name="HRLogin"),
    path('HRLogout/', LogoutView.as_view(template_name='hrAppLogout.html'),
         name="HRLogout"),

    path('ListaEmpleados/', ListarEmpleados.as_view(), name="ListaEmpleados"),
    path('CrearEmpleados/', CrearEmpleados.as_view(), name="CrearEmpleados"),
    path('ActualizarEmpleados/<int:pk>',
         ActualizarEmpleados.as_view(), name="ActualizarEmpleados"),
    path('BorrarEmpleados/<int:pk>',
         BorrarEmpleados.as_view(), name="BorrarEmpleados"),
    path('BusquedaEmpleado/', BusquedaEmpleado.as_view(), name="BusquedaEmpleado"),

    path('ListaClientes/', ListarClientes.as_view(), name="ListaClientes"),
    path('CrearClientes/', CrearClientes.as_view(), name="CrearClientes"),
    path('ActualizarClientes/<int:pk>',
         ActualizarClientes.as_view(), name="ActualizarClientes"),
    path('BorrarClientes/<int:pk>', BorrarClientes.as_view(), name="BorrarClientes"),
    path('BusquedaCliente/', BusquedaCliente.as_view(), name="BusquedaCliente"),
]
