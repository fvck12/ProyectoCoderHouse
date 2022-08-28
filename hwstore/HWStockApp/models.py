from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    stock = models.IntegerField()
    precio = MoneyField(
        decimal_places=2,
        default=1,
        default_currency='USD',
        max_digits=11,
    )
    Foto = models.ImageField(upload_to="Productos/", height_field=None,
                             width_field=None, max_length=None, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nombre}'
    categoria_opcion = (
        ('C', 'Construccion',),
        ('P', 'Pintura',),
        ('B', 'Bannos',),
        ('M', 'Madera',),
        ('H', 'Hogar',),
        ('J', 'Jardin',),
        ('E', 'Electricidad',),
        ('O', 'Otros',),
    )
    categoria = models.CharField(
        max_length=1, choices=categoria_opcion, blank=True
    )
