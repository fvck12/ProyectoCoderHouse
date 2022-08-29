from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from HWStoreApp.views import HWStoreInicio

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', HWStoreInicio, name="HWStoreInicio"),    
    path('HWStoreApp/', include('HWStoreApp.urls')),
    path('HWStockApp/', include('HWStockApp.urls')),
    path('accounts/', include('Accounts.urls')),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
