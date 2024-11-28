
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    path("index", views.index, name="index"),
    path('celulares/iphone16pro', views.iphone16pro, name='iphone16pro'),
    path('celulares/iphone16', views.iphone16, name='iphone16'),
    path('celulares/iphone15', views.iphone15, name='iphone15'),
    #3 
    path('celulares/samsungS24', views.samsungS24, name='samsungS24'),
    #6
    path('celulares/samsungS23', views.samsungS23, name='samsungS23'),
    path('celulares/samsungS24FE', views.samsungS24FE, name='samsungS24FE'),
    path('celulares/samsungS24Ultra', views.samsungS24Ultra, name='samsungS24Ultra'),
    #9
    path('celulares/samsungS23FE', views.samsungS23FE, name='samsungS23FE'),
    path('celulares/POCOX6Pro', views.POCOX6Pro, name='POCOX6Pro'),
    path('celulares/samsungA15', views.samsungA15, name='samsungA15'),
    #12
    path('celulares/redmiNote13Pro', views.redmiNote13Pro, name='redmiNote13Pro'),
    path('celulares/redmiNote13', views.redmiNote13, name='redmiNote13'),
    path('celulares/edge50Pro', views.edge50Pro, name='edge50Pro'),
    #15
    path('celulares/motorolaE14', views.motorolaE14, name='motorolaE14'),
    path('celulares/galaxyA55', views.galaxyA55, name='galaxyA55'),
    #18
    path('celulares/samsungA15Ligh', views.samsungA15Ligh, name='samsungA15Ligh'),
    path('celulares/samsungA05', views.samsungA05, name='samsungA05'),
    path('celulares/xiaomi14T', views.xiaomi14T, name='xiaomi14T'),
    #21
    path('celulares/iphone13', views.iphone13, name='iphone13'),
    path('celulares/iphone13mini', views.iphone13mini, name='iphone13mini'),
    path('celulares/iphone11', views.iphone11, name='iphone11'),

    path('', views.lista_productos, name='lista_productos'),
    path('agregar<int:producto_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    path('carro', views.ver_carro, name='ver_carro'),
    path('productos', views.productos, name='productos'),
    path('compra', views.compra, name='compra'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('gracias', views.gracias, name='gracias'),
    path('carro/reducir/<int:item_id>/', views.reducir_cantidad, name='reducir_cantidad'),
    path('carro/incrementar/<int:item_id>/', views.incrementar_cantidad, name='incrementar_cantidad'),
    path('carro/eliminar/<int:item_id>/', views.eliminar_del_carro, name='eliminar_del_carro'),
    

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
