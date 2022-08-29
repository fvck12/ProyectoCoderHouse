from django.contrib import admin
from .models import Usuario, Cliente, Empleado

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'fecha_nacimiento',
                    'email', 'direccion', 'telefono']


class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['puesto']


class ClientesAdmin(admin.ModelAdmin):
    list_display = ['numero_socio']

# Register your models here.

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Empleado, EmpleadosAdmin)



