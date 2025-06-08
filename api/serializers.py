from rest_framework import serializers
from .models import Tienda, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TiendaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Tienda
        fields = ['id', 'nombre', 'productos']
