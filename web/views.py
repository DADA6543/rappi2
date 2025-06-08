from django.shortcuts import render
from .forms import RegistroForm
from django.contrib.auth import login
from django.shortcuts import redirect

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

def registro(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            if form.cleaned_data['is_superuser']:
                user.is_superuser = True
                user.is_staff = True
            user.save()

            login(request, user)

            # Redirigir según el tipo de usuario
            if user.is_superuser:
                return redirect('/admin/')  # O usar reverse('admin:index')
            else:
                return redirect('/')  # Cambia '/' por tu home si es otra ruta
        else:
            messages.error(request, "Hubo un error en el formulario.")
    else:
        form = CustomRegisterForm()

    return render(request, 'register.html', {'form': form})
