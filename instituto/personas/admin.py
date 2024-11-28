from django.contrib import admin
from .models import Producto
# Register your models here.
from .models import Orden, DetalleOrden

admin.site.register(Producto)

admin.site.register(DetalleOrden)

