from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, ItemCarro
# Create your views here.

def index(request):
    context={}
    return render(request,"personas/index.html",context)

def iphone15(request):
    # Busca el producto por ID (1 en este caso)
    producto = get_object_or_404(Producto, id=1)
    context = {'producto': producto}
    return render(request, 'personas/iphone15.html', context)


def iphone16(request):
    producto = get_object_or_404(Producto, id=2)  # Cambia al ID del iPhone 16
    context = {'producto': producto}
    return render(request, 'personas/iphone16.html', context)

def iphone16pro(request):
    producto = get_object_or_404(Producto, id=3)  # Cambia al ID del iPhone 16 Pro
    context = {'producto': producto}
    return render(request, 'personas/iphone16pro.html', context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'personas/detalle_producto.html', {'producto': producto})

# Vista para agregar al carro
def agregar_al_carro(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    item, created = ItemCarro.objects.get_or_create(producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carro')

# Vista para ver el carro
def ver_carro(request):
    items = ItemCarro.objects.all()
    total = sum(item.subtotal() for item in items)
    return render(request, 'personas/ver_carro.html', {'items': items, 'total': total})



def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'personas/lista_productos.html', {'productos': productos})