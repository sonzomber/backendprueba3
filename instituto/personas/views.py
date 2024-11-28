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
    productos = Producto.objects.all()  
    producto = productos.filter(id=1).first()  
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone15.html', context)


def iphone16(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=2).first() 
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone16.html', context)

def iphone16pro(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=3).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone16pro.html', context)



#ACA

def samsungS24(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=4).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS24.html', context)


def samsungS23(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=5).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS23.html', context)

def samsungS24FE(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=6).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS24FE.html', context)

def samsungS24Ultra(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=7).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS24Ultra.html', context)


def samsungS23FE(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=8).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungS23FE.html', context)

def POCOX6Pro(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=9).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/POCOX6Pro.html', context)

def samsungA15(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=15).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungA15.html', context)


def redmiNote13Pro(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=10).first() 
    context = {'producto': producto}
    return render(request, 'personas/celulares/redmiNote13Pro.html', context)

def edge50Pro(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=12).first()
    context = {'producto': producto}
    return render(request, 'personas//celulares/edge50Pro.html', context)

def motorolaE14(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=13).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/motorolaE14.html', context)


def galaxyA55(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=14).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/galaxyA55.html', context)

def samsungA15Ligh(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=16).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungA15Ligh.html', context)

def samsungA05(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=17).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/samsungA05.html', context)


def xiaomi14T(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=18).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/xiaomi14T.html', context)

def iphone13(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=19).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone13.html', context)

def iphone13mini(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=20).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone13mini.html', context)

def iphone11(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=21).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/iphone11.html', context)

def redmiNote13(request):
    productos = Producto.objects.all()  
    producto = productos.filter(id=11).first()
    context = {'producto': producto}
    return render(request, 'personas/celulares/redmiNote13.html', context)



#--------------------------------------------------------------------------------


def agregar_al_carro(request, producto_id):

    productos = Producto.objects.all()
    producto = productos.filter(id=producto_id).first()

    # Verificar si hay stock disponible
    if producto.stock > 0:
       
        item, created = ItemCarro.objects.get_or_create(producto=producto)
        if created:  #
            item.cantidad = 1
        elif item.cantidad < producto.stock:  
            item.cantidad += 1
        else:
            messages.warning(request, "No hay suficiente stock disponible.")
            return redirect('ver_carro')
        
        # Guardar el ítem y actualizar el stock
        item.save()
        producto.stock -= 1
        producto.save()
        messages.success(request, f"Se agregó {producto.nombre} al carrito.")
    else:
        messages.error(request, "Este producto está agotado.")
    
    return redirect('ver_carro')

def compra(request):
    producto = Producto.objects.all() 
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
    
    items = ItemCarro.objects.all()

      # Buscar el ítem específico por su id
    item = next((i for i in items if i.id == item_id), None)


    producto = item.producto

   
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()  

    producto.stock += 1
    producto.save()

    return redirect('ver_carro')