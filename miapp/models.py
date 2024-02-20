from django.db import models

# Create your models here.
class Producto (models.Model):
    
        nombre = models.CharField(max_length=40)
        precio = models.IntegerField()

        def __str__(self):
             return f"{self.nombre}"
    
   
    
class Cliente (models.Model):
        
    nombre=models.CharField(max_length=40)
    dni=models.IntegerField()
    
class Mediosdepago(models.Model):
        
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField()
    tarjetas=models.CharField(max_length=40)
class Ofertas(models.Model):
        
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField()  
    fechamax= models.IntegerField()  
    
   