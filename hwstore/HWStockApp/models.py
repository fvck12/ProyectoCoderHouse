from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


class Productos(models.Model):
    nombre = models.CharField(max_length=20)
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
