from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    TiendaViewSet,
    ProductoViewSet,
    ComidaViewSet,
    RopaViewSet,
    UtilesViewSet,
)

router = DefaultRouter()
router.register(r'tiendas',   TiendaViewSet,    basename='tiendas')
router.register(r'productos', ProductoViewSet,  basename='productos')
router.register(r'comida',    ComidaViewSet,    basename='comida')
router.register(r'ropa',      RopaViewSet,      basename='ropa')
router.register(r'utiles',    UtilesViewSet,    basename='utiles')

urlpatterns = [
    path('', include(router.urls)),
]