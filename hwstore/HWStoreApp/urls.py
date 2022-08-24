from django.urls import path
from HWStoreApp.views import inicio, login_request, registro, access_denied

urlpatterns = [
    path('', inicio, name="inicio"),
    path('AccessDenied/', access_denied, name="AccessDenied"),
    path('HWStorelogin/', login_request, name="HWStorelogin"),
    path('registro/', registro, name="Registro"),
]
