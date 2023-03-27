from django.shortcuts import render, redirect
from .models import Users
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def login (request):
    if request.metod == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Bienvenido ' + Users.first_name)
            return render(request, 'home.html')
        else:
            messages.error(request, 'Error de autenticacion')
            return redirect('users/login.html', {'alarma': 'Error de autenticacion'})
    else:
        return render(request, 'users/login.html')


# -------DESACTIVAR USUARIO-------

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


# -------REGISTRAR USUARIO-------

def Register(request):
    if request.method == 'POST':
        pass
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
