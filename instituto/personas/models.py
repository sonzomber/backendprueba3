from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MiModelo(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')  




class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

class ItemCarro(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    


class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden #{self.id} - {self.usuario.username}"

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)




    def subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Orden #{self.orden.id}"