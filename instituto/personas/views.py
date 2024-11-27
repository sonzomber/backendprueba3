from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, ItemCarro
from django.contrib import messages
# Create your views here.

def index(request):
    context={}
    return render(request,"personas/index.html",context)

def productos(request):
    context={}
    return render(request,"personas/productos.html",context)

#-------------------------------------------------------------------------------------
def iphone15(request):
    producto = get_object_or_404(Producto, id=1)
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone15.html', context)


def iphone16(request):
    producto = get_object_or_404(Producto, id=2)  
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone16.html', context)

def iphone16pro(request):
    producto = get_object_or_404(Producto, id=3)
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone16pro.html', context)



#ACA

def samsungS24(request):
    producto = get_object_or_404(Producto, id=4)
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS24.html', context)


def samsungS23(request):
    producto = get_object_or_404(Producto, id=5)  
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS23.html', context)

def samsungS24FE(request):
    producto = get_object_or_404(Producto, id=6)
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS24FE.html', context)

def samsungS24Ultra(request):
    producto = get_object_or_404(Producto, id=7)
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS24Ultra.html', context)


def samsungS23FE(request):
    producto = get_object_or_404(Producto, id=8)  
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS23FE.html', context)

def POCOX6Pro(request):
    producto = get_object_or_404(Producto, id=9)
    context = {'producto': producto}
    return render(request, 'personas/celulares/POCOX6Pro.html', context)

def samsungA15(request):
    producto = get_object_or_404(Producto, id=15)
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungA15.html', context)


def redmiNote13Pro(request):
    producto = get_object_or_404(Producto, id=10)  
    context = {'producto': producto}
    return render(request, 'personas/celulares/redmiNote13Pro.html', context)

def edge50Pro(request):
    producto = get_object_or_404(Producto, id=12)
    context = {'producto': producto}
    return render(request, 'personas//celulares/edge50Pro.html', context)

def motorolaE14(request):
    producto = get_object_or_404(Producto, id=13)
    context = {'producto': producto}
    return render(request, 'personas/celulares/motorolaE14.html', context)


def galaxyA55(request):
    producto = get_object_or_404(Producto, id=14)  
    context = {'producto': producto}
    return render(request, 'personas/celulares/galaxyA55.html', context)

def samsungA15Ligh(request):
    producto = get_object_or_404(Producto, id=16)
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungA15Ligh.html', context)

def samsungA05(request):
    producto = get_object_or_404(Producto, id=17)
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungA05.html', context)


def xiaomi14T(request):
    producto = get_object_or_404(Producto, id=18)  
    context = {'producto': producto}
    return render(request, 'personas/celulares/xiaomi14T.html', context)

def iphone13(request):
    producto = get_object_or_404(Producto, id=19)
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone13.html', context)

def iphone13mini(request):
    producto = get_object_or_404(Producto, id=20)
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone13mini.html', context)

def iphone11(request):
    producto = get_object_or_404(Producto, id=21)  
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone11.html', context)

def redmiNote13(request):
    producto = get_object_or_404(Producto, id=11)
    context = {'producto': producto}
    return render(request, 'personas/celulares/redmiNote13.html', context)



#--------------------------------------------------------------------------------


def agregar_al_carro(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
  
    if producto.stock > 0:
        item, created = ItemCarro.objects.get_or_create(producto=producto)
        if created or item.cantidad < producto.stock:
            item.cantidad += 1
            item.save()
            producto.stock -= 1  # Reducir el stock
            producto.save()
            messages.success(request, f"Se agregó {producto.nombre} al carrito.")
        else:
            messages.warning(request, "No hay suficiente stock disponible.")
    else:
        messages.error(request, "Este producto está agotado.")
    
    return redirect('ver_carro')

def compra(request):
    producto = get_object_or_404(Producto, id=11)
    context = {'producto': producto}
    return render(request, 'personas/compra.html', context)



def ver_carro(request):
    items = ItemCarro.objects.all()
    total = sum(item.subtotal() for item in items)
    return render(request, 'personas/ver_carro.html', {'items': items, 'total': total})



def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'personas/lista_productos.html', {'productos': productos})


def reducir_cantidad(request, item_id):
    item = get_object_or_404(ItemCarro, id=item_id)
    producto = item.producto

    # Reducir la cantidad en el carrito
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()  

 
    producto.stock += 1
    producto.save()

    return redirect('ver_carro')  