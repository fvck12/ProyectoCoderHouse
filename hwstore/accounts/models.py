from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_empleado = models.BooleanField(default=False)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    def edad(self):
        import datetime
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25)
    edad = property(edad)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.CharField(max_length=80, blank=True)
    telefono = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name}'


class Cliente(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    numero_socio = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return f'{self.numero_socio}'

class Empleado(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    puesto = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f'{self.puesto}'