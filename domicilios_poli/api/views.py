from rest_framework import viewsets
from .models import Tienda, Producto
from .serializers import TiendaSerializer, ProductoSerializer


class TiendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver y editar todas las tiendas.
    """
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer


class ComidaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para productos de la tienda de comida.
    Filtra automáticamente por tienda__nombre='tienda_comida'.
    """
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.filter(tienda__nombre='tienda_comida')


from rest_framework import viewsets
from .models import Tienda, Producto
from .serializers import TiendaSerializer, ProductoSerializer

class TiendaViewSet(viewsets.ModelViewSet):
    """
    API para ver y editar tiendas.
    """
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    Endpoint genérico para todos los productos.
    Permite filtrar por `?tienda__nombre=` si se desea.
    """
    serializer_class = ProductoSerializer

    def get_queryset(self):
        qs = Producto.objects.all()
        nombre_tienda = self.request.query_params.get('tienda__nombre')
        if nombre_tienda:
            qs = qs.filter(tienda__nombre=nombre_tienda)
        return qs

class ComidaViewSet(viewsets.ModelViewSet):
    """
    Productos de la tienda de comida.
    """
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.filter(tienda__nombre='tienda_comida')

class RopaViewSet(viewsets.ModelViewSet):
    """
    Productos de la tienda de ropa.
    """
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.filter(tienda__nombre='tienda_ropa')

class UtilesViewSet(viewsets.ModelViewSet):
    """
    Productos de la tienda de útiles.
    """
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.filter(tienda__nombre='tienda_utiles')