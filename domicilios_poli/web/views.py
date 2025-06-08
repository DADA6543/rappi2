
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomRegisterForm

def home(request):
    return render(request, 'home.html')

def comidas(request):
    return render(request, 'tienda-comida.html')

def carrito(request):
    return render(request, 'carrito.html')

def ropa(request):
    return render(request, 'tienda-ropa.html')

def utiles(request):
    return render(request, 'tienda-utiles.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')

def admin_comida(request):
    return render(request, 'admin_comida.html')

def admin_utiles(request):
    return render(request, 'admin_utiles.html')

def admin_ropa(request):
    return render(request, 'admin_ropa.html')

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            if form.cleaned_data['is_superuser']:
                user.is_superuser = True
                user.is_staff = True
            user.save()
            messages.success(request, "Usuario creado correctamente.")
            return redirect('login')  # O tu vista de inicio de sesión
    else:
        form = CustomRegisterForm()
        return render(request, 'register.html', {'form': form})
