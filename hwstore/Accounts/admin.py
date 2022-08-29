from django.contrib import admin
from .models import User, Profile

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'fecha_nacimiento',
                    'email', 'direccion', 'telefono']

# Register your models here.

admin.site.register(User, UsuarioAdmin)
admin.site.register(Profile)