from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


############################## Login ##############################

def LoginStore(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect("/HWStoreApp/")
            else:
                return redirect("/HWStoreApp/")
    form = AuthenticationForm()
    return render(request, "HWStoreLogin.html", {"form": form})


############################## Pagina principal ##############################


def HWStoreInicio(request):

    return render(request, "HWStoreIndex.html")
