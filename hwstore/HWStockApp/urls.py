"""hwstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from HWStockApp.views import CrearProducto, BusquedaProducto, ListarProductos, BorrarProducto, ActualizarProducto
from HWStockApp.views import HWStockAppInicio,login_request, registro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HWStockAppInicio, name="HWStockIndex"),
    path('login/', login_request, name="Login"),
    path('registro/', registro, name="Registro"),
    path('logout/', LogoutView.as_view(template_name='hrAppLogout.html'), name="Logout"),

    path('formProducto/', CrearProducto.as_view(), name="CrearProductos"),
    path('busquedaProductos/', BusquedaProducto.as_view(), name="busquedaProductos"),
    path('listaProductos/', ListarProductos.as_view(), name="listaProductos"),
    path('eliminarProducto/<int:pk>', BorrarProducto.as_view(), name="eliminarProducto"),
    path('editarProducto/<int:pk>', ActualizarProducto.as_view(), name="editarProducto"),

]
