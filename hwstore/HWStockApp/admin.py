from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Productos

class ProductosAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', "marca", 'stock', 'precio', 'Foto']

# Register your models here.
admin.site.register(Productos, ProductosAdmin)