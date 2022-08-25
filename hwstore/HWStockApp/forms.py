from tkinter import ALL
from django import forms
from HWStockApp.models import Productos


class FormProductos(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ('__all__')
