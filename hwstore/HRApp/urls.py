from django.urls import path
from HRApp.views import ListarEmpleados, BusquedaEmpleado, CrearEmpleados, ActualizarEmpleados, BorrarEmpleados
from HRApp.views import hrAppInicio, login_request, registro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', hrAppInicio, name="HRAppInicio"),
    path('login/', login_request, name="Login"),
    path('registro/', registro, name="Registro"),
    path('logout/', LogoutView.as_view(template_name='hrAppLogout.html'), name="Logout"),
    
    path('ListaEmpleados/', ListarEmpleados.as_view(), name="ListaEmpleados"),
    path('CrearEmpleados/', CrearEmpleados.as_view(), name="CrearEmpleados"),
    path('ActualizarEmpleados/<int:pk>', ActualizarEmpleados.as_view(), name="ActualizarEmpleados"),
    path('BorrarEmpleados/<int:pk>', BorrarEmpleados.as_view(), name="BorrarEmpleados"),
    path('BusquedaEmpleado/', BusquedaEmpleado.as_view(), name="BusquedaEmpleado"),
]