from django import forms

class productoform(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    precio=forms.IntegerField(required=True)
    
    
class clienteform(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    dni=forms.IntegerField(required=True)
    
    

class ofertaform (forms.Form):
        
    nombre=forms.CharField(max_length=50, required=True)
    precio=forms.IntegerField(required=True) 
    fechamax= forms.IntegerField(required=True) 
    
    