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

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            return redirect('/home/')  # Puedes redirigir al home u otra vista
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
