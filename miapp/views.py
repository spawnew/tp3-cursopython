from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return render (request,"miapp/home.html")
def productos(request):
      contexto = {'productos': Producto.objects.all()}
      return render (request,"miapp/productos.html",contexto)
     
def mediosdepagos(request):
    
    return render (request,"miapp/mediosdepagos.html")
     
def clientes(request):
      contexto = {'clientes': Cliente.objects.all()}
      return render (request,"miapp/clientes.html",contexto)
def ofertas(request):
    contexto = {'ofertas': Ofertas.objects.all()}
    return render (request,"miapp/ofertas.html",contexto)
def ofertaForm(request):
    if request.method =="POST":
        miform = ofertaform(request.POST)
        if miform.is_valid():  
            ofertanombre = miform.cleaned_data.get( "nombre" )
            ofertaprecio = miform.cleaned_data.get( "precio" )
            ofertafechamax = miform.cleaned_data.get( "fechamax" )
            oferta= Ofertas( nombre=ofertanombre , precio=ofertaprecio ,fechamax=ofertafechamax)
            oferta.save()
            return render(request, "miapp/home.html")
        else:
        
            return render(request, "miapp/ofertaForm.html", {"form": miform})
    else:
        miform = ofertaform()
    return render(request, "miapp/ofertaForm.html", {"form": miform})

  
def productoForm(request):
    if request.method =="POST":
        miform = productoform(request.POST)
        if miform.is_valid():  
            productonombre = miform.cleaned_data.get( "nombre" )
            productoprecio = miform.cleaned_data.get( "precio" )
            producto= Producto( nombre=productonombre , precio=productoprecio)
            producto.save()
            return render(request, "miapp/home.html")
        else:
        
            return render(request, "miapp/productoForm.html", {"form": miform})
    else:
        miform = productoform()
    return render(request, "miapp/productoForm.html", {"form": miform})

def clienteForm(request):
    if request.method =="POST":
        miform = clienteform(request.POST)
        if miform.is_valid():  
            clientenombre = miform.cleaned_data.get( "nombre" )
            clientedni = miform.cleaned_data.get( "dni" )
            cliente= Cliente( nombre= clientenombre , dni=clientedni)
            cliente.save()
            return render(request, "miapp/home.html")
        else:
        
            return render(request, "miapp/clienteform.html", {"form": miform})
    else:
        miform = clienteform()
    return render(request, "miapp/clienteform.html", {"form": miform})

def mediosdepagoform(request):
    if request.method =="POST":
        miform = mediosdepagoform(request.POST)
        if miform.is_valid():  
            medionombre = miform.cleaned_data.get ( "nombre" )
            medioprecio = miform.cleaned_data.get ( "precio" )
            mediotarjeta = miform.cleaned_data.get ( "tarjeta" )
            mediosdepago= Mediosdepago( nombre= medionombre , precio=medioprecio , tarjeta=mediotarjeta)
            mediosdepago.save()
            return render(request, "miapp/home.html")
        else:
            return render(request, "miapp/mediosdepagoform.html", {"form": miform})
    else:
        miform = mediosdepagoform()
    return render(request, "miapp/mediosdepagoform.html", {"form": miform})



def buscar(request):
    return render(request, "miapp/buscar.html")

def buscarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"productos": productos }
        return render(request, "miapp/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")



