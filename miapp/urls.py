from django.urls import path
from .views import *


urlpatterns = [
   path('', home, name="home"),
    path('clientes/', clientes, name="clientes"),
   path('mediosdepagos/', mediosdepagos, name="mediosdepagos"),
   path('ofertas/', ofertas, name="ofertas"),
   path('productos/', productos, name="productos"),
   path('productoform/', productoForm, name="productoform"),
   path('clienteform/', clienteForm, name="clienteform"),
    path('ofertaform/', ofertaForm, name="ofertaform"),
    
    path('buscar/', buscar, name="buscar"),
    path('buscarProductos/', buscarProductos, name="buscarProductos"),
 
   
];