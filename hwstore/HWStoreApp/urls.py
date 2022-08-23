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
from HWStoreApp.views import inicio, login_request, registro, access_denied

urlpatterns = [
    path('', inicio, name="inicio"),
    path('AccessDenied/', access_denied, name="AccessDenied"),
    path('login/', login_request, name="Login"),
    path('registro/', registro, name="Registro"),
]
