from xmlrpc.client import Boolean
from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=25, blank=False)
    apellido = models.CharField(max_length=25, blank=False)
    sexo_opcion = (
        ('F', 'Femenino',),
        ('M', 'Masculino',),
        ('O', 'Otro',),
    )
    sexo = models.CharField(
        max_length=1, choices=sexo_opcion, blank=True
    )
    fecha_nacimiento = models.DateField(null=True, blank=True)
    dni = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    direccion = models.CharField(max_length=80, blank=False)
    telefono = models.IntegerField(blank=True)

    def edad(self):
        import datetime
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25)
    edad = property(edad)

    class Meta():
        abstract = True


class Empleado(Persona):
    puesto = models.CharField(max_length=25)
    horario_opcion = (
        ('M', 'Matutino',),
        ('V', 'Vespertino',),
    )
    horario = models.CharField(
        max_length=1, choices=horario_opcion, blank=False
    )
    salario = MoneyField(
        decimal_places=2,
        default=1,
        default_currency='USD',
        max_digits=11,
    )
    foto_empleado = models.ImageField(
        upload_to="Empleados/", height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nombre}'


class Cliente(Persona):
    nombre_usuario = models.CharField(max_length=8, blank=False)
    foto_cliente = models.ImageField(
        upload_to="Clientes/", height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nombre}'
