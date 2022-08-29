from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import Cliente, Empleado, Usuario


class ClienteSignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField(label="Correo", required=True)
    username = forms.CharField(label="Usuario", required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirma Contraseña", widget=forms.PasswordInput)
    fecha_nacimiento = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
    telefono = forms.CharField(required=False)
    numero_socio = forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'fecha_nacimiento',
                  'direccion', 'telefono', 'numero_socio']

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.password1 = self.cleaned_data.get('password1')
        user.password2 = self.cleaned_data.get('password2')
        user.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        user.direccion = self.cleaned_data.get('direccion')
        user.telefono = self.cleaned_data.get('telefono')
        user.is_cliente = True
        user.save()
        cliente = Cliente.objects.create(user=user)
        cliente.numero_socio = self.cleaned_data.get('numero_socio')
        cliente.save()
        return user


class EmpleadoSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    fecha_nacimiento = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
    telefono = forms.CharField(required=False)
    puesto = forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['first_name', 'last_name', 'fecha_nacimiento',
                  'direccion', 'telefono', 'puesto']

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        user.direccion = self.cleaned_data.get('direccion')
        user.telefono = self.cleaned_data.get('telefono')
        user.is_empleado = True
        user.save()
        empleado = Empleado.objects.create(user=user)
        empleado.puesto = self.cleaned_data.get('puesto')
        empleado.save()
        return user
