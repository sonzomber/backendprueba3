
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    path("index", views.index, name="index"),
    path('iphone16pro', views.iphone16pro, name='iphone16pro'),
    path('iphone16', views.iphone16, name='iphone16'),
    path('iphone15', views.iphone15, name='iphone15'),
    path('', views.lista_productos, name='lista_productos'),
    path('producto<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('agregar<int:producto_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    path('carro', views.ver_carro, name='ver_carro'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

