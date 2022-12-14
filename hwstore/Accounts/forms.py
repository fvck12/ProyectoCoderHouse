import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Accounts.models import Profile, User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    telefono = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'direccion', 'telefono']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
