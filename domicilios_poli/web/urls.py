from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('comidas/', views.comidas, name='comidas'),
    path('carrito/', views.carrito, name='carrito'),
    path('ropa/', views.ropa, name='ropa'),
    path('utiles/', views.utiles, name='utiles'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),  # Evita llamar la vista como 'admin' porque puede chocar con el admin de Django
    path('admin_comida/', views.admin_comida, name='admin_comida'),
    path('admin_utiles/', views.admin_utiles, name='admin_utiles'),
    path('admin_ropa/', views.admin_ropa, name='admin_ropa'),
    # Otras rutas de tu proyecto...
    path('api/', include('api.urls')),    # <— así montas /api/comida/, /api/ropa/, etc.
        # si usas una app 'web' para las plantillas
    
]
