from django.shortcuts import render

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
