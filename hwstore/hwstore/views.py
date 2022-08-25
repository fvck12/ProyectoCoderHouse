from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registro(request):    
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "HWStoreIndex.html", {"mensaje": "Se ha registrado!"})
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})