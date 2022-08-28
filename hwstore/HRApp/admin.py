from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Empleado, Cliente


class EmpleadosAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'edad', 'sexo', 'fecha_nacimiento', 'dni',
                    'email', 'direccion', 'telefono', 'salario', 'puesto', 'horario', 'foto_empleado']


class ProductosAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', "marca", 'stock', 'precio', 'Foto']


class ClientesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'sexo', 'fecha_nacimiento', 'dni',
                    'email', 'direccion', 'telefono', 'username', 'foto_cliente', 'is_active']
        


# Register your models here.
admin.site.register(Empleado, EmpleadosAdmin)
admin.site.register(Cliente, ClientesAdmin)
