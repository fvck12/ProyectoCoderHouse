from enum import auto
from django import forms
from django.contrib.auth.models import User


class CreateClientForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre', max_length=25)
    last_name = forms.CharField(label='Apellido', max_length=25)
    username = forms.CharField(label='Usuario', max_length=10)
    email = forms.EmailField(label='Correo')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    repeat_password = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)
    # Here we add the extra form fields that we will use to create another model object
    dni = forms.IntegerField(required=False)
    fecha_nacimiento = forms.DateField(required=False)
    direccion = forms.CharField(required=False)
    telefono = forms.IntegerField(required=False)
    foto_cliente = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]
