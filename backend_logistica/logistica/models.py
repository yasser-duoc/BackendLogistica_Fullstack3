from django.db import models

class CentroAcopio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    capacidad_maxima = models.IntegerField()
    #requerimiento de ubicación geográfica<-- se requiere no me acuerdo en que XD
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    #Tipos: ropa, alimento, insumos médicos, higiene
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    centro = models.ForeignKey(CentroAcopio, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)