from django.contrib import admin
from django.urls import path, include
from HWStoreApp import urls as store_url
from HRApp import urls as hr_url
from HWStockApp import urls as hwstock_url
from hwstore.views import Register
from django.conf import settings
from django.conf.urls.static import static
from HWStoreApp.views import HWStoreInicio
urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HWStoreInicio, name="HWStoreInicio"),
    path('HWStoreApp/', include(store_url)),
    path('HRApp/', include(hr_url)),
    path('HWStockApp/', include(hwstock_url)),
    path('Registro/', Register, name="Registro"),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
