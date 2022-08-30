from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from Accounts.models import User, Profile
from django.contrib.auth.decorators import login_required 
from Accounts.forms import UserUpdateForm, ProfileUpdateForm

# Pagina de inicio

def home(request):
    return render(request, 'HWStoreIndex.html')

# Registro de usuarios

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'El usuario ya existe!')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'El correo ya esta registrado')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password,
                                                email=email, first_name=first_name, last_name=last_name)
                user.save()
                user = User.objects.get(username=username)
                profile = Profile(user=user)
                profile.save()
                
                return redirect('login')

        else:
            messages.info(request, 'Las contraseñas no coinciden')
            return redirect(register)

    else:
        return render(request, 'Register.html')

# Login de usuarios

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Usuario o contraseña inválidos')
            return redirect('login')

    else:
        return render(request, 'Login.html')
    
def logout_user(request):
    auth.logout(request)
    return redirect('home')

# Edicion de perfil de usuarios

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Su cuenta fue actualizada!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Account_Profile.html', context)