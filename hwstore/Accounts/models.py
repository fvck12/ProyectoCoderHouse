from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    def edad(self):
        import datetime
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25)
    edad = property(edad)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.CharField(max_length=80, blank=True)
    telefono = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f'{self.username}'


class Profile(models.Model):
    # Delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='Clientes')

    def __str__(self):
        # show how we want it to be displayed
        return f'{self.user.username} Profile'
        # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image