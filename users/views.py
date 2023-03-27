from django.shortcuts import render, redirect
from .models import Users
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from users.forms import RegisterForm


def login(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Lógica de autenticación de usuario aquí
            return render(request, 'users/home.html')
        else:
            # Si el formulario es inválido, mostrarlo nuevamente con los errores
            return render(request, 'users/login.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'users/login.html', {'form': form})



# -------DESACTIVAR USUARIO-------

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


# -------REGISTRAR USUARIO-------



def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Lógica de creación de usuario aquí
            return render(request, 'users/login.html', {'alarma': 'Usuario registrado'})
        else:
            # Si el formulario es inválido, mostrarlo nuevamente con los errores
            return render(request, 'users/register.html', {'form': form})
    else:
        # Si la solicitud HTTP es un método GET, mostrar el formulario vacío
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
