from django.test import TestCase
from rest_framework.test import APIClient
from .models import Producto

class LogisticaTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Crear un producto de prueba
        Producto.objects.create(nombre="Insumos Médicos", categoria="Salud")

    def test_get_productos_sin_token(self):
        """Verifica que no se puede acceder a productos sin estar autenticado"""
        response = self.client.get('/api/logistica/productos/')
        self.assertEqual(response.status_code, 403)