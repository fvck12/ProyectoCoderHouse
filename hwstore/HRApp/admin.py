from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Empleado, Cliente
from django.contrib.auth.models import User


class EmpleadosAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['edad', 'sexo', 'fecha_nacimiento', 'dni', 'direccion',
                    'telefono', 'salario', 'puesto', 'horario', 'foto_empleado']


class ProductosAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', "marca", 'stock', 'precio', 'Foto']


class UserInline(admin.TabularInline):
    model = User
    fk_name = 'id'

class ClientesAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Cliente
    inlines = [UserInline]
    # list_display = ['user_id', 'dni', 'fecha_nacimiento',
    #                 'direccion', 'telefono', 'foto_cliente']

# Register your models here.
admin.site.register(Empleado, EmpleadosAdmin)
admin.site.register(Cliente, ClientesAdmin)
