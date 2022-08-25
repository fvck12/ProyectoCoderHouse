from django.urls import path
from HWStoreApp.views import HWStoreInicio, LoginStore
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HWStoreInicio, name="HWStoreInicio"),
    path('LoginStore/', LoginStore, name="LoginStore"),
    path('LogoutStore/', LogoutView.as_view(template_name='HWStoreLogout.html'),
         name="LogoutStore"),
]
