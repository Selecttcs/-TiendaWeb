from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_usuario) + str(self.name)
    
class Producto(models.Model):
    name = models.CharField(max_length=100) 
    sku = models.CharField(primary_key=True, max_length=3)
    precio = models.IntegerField(max_length=3)

    def __str__(self):
        return str(self.sku) + str(self.name)

class Venta(models.Model):
    id_venta = models.CharField(primary_key=True,max_length=5)
    sku = models.CharField(max_length=3)
    cantidad = models.IntegerField(max_length=3)
    def __str__(self):
        return str(self.id_venta) + str(self.cantidad)
    
class Oferta(models.Model):
    id_oferta = models.CharField(primary_key=True,max_length=3)
    nombre = models.CharField(max_length=100)   
    contacto = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=3)
    costo = models.IntegerField(max_length=10)
    
    
    