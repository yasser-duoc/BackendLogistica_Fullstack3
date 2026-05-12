from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializerClase = ProductoSerializer
    permisosClases = [permissions.IsAdminUser]
