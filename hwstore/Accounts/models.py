from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.CharField(max_length=80, blank=True)
    telefono = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f'{self.username}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='Clientes')

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)