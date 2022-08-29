from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import Usuario
from .forms import ClienteSignUpForm, EmpleadoSignUpForm

# Create your views here.

def register(request):
    return render(request, 'HWStoreRegister.html')


class ClienteRegistro(CreateView):
    model = Usuario
    form_class = ClienteSignUpForm
    template_name = 'HWStoreRegister.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/HWStoreApp/')


class EmpleadoRegistro(CreateView):
    model = Usuario
    form_class = EmpleadoSignUpForm
    template_name = 'EmpleadoRegistro.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/HWStoreApp/')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/HWStoreApp/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'HWStoreLogin.html', context={'form': AuthenticationForm()})


def logout_user(request):
    logout(request)
    return redirect('/HWStoreApp/')
