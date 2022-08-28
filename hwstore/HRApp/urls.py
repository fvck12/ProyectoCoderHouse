from django.urls import path
from HRApp.views import ListarEmpleados, BusquedaEmpleado, CrearEmpleados, ActualizarEmpleados, BorrarEmpleados
from HRApp.views import ListarUsuario, BusquedaUsuario, CrearUsuario, ActualizarUsuario, BorrarUsuario
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

    path('ListaUsuario/', ListarUsuario.as_view(), name="ListaUsuario"),
    path('CrearUsuario/', CrearUsuario.as_view(), name="CrearUsuario"),
    path('ActualizarUsuario/<int:pk>',
         ActualizarUsuario.as_view(), name="ActualizarUsuario"),
    path('BorrarUsuario/<int:pk>', BorrarUsuario.as_view(), name="BorrarUsuario"),
    path('BusquedaUsuario/', BusquedaUsuario.as_view(), name="BusquedaUsuario"),
]
