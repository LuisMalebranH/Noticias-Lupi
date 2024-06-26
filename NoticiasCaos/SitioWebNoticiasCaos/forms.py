from django import forms
from .models import Articulo, Categoria

from django.forms import ModelForm

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = {'tituloArticulo', 
                    'contenidoArticulo', 
                    'sinopsisArticulo', 
                    'imagenArticulo',
                    'usuarioAutor'} 

        widgets = { 
                    'sinopsisArticulo': forms.TextInput(attrs={'class': 'form-control' }),
                    'contenidoArticulo': forms.TextInput(attrs={'class': 'form-control' }), 
                    'tituloArticulo' : forms.TextInput(attrs={'class': 'form-control' }),
                    }

# Arreglar form de Edicion despues
""" 
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = {'tituloArticulo', 
                    'contenidoArticulo', 
                    'sinopsisArticulo', 
                    'imagenArticulo',
                    'usuarioAutor'} 

        widgets = { 
                    'sinopsisArticulo': forms.TextInput(attrs={'class': 'form-control' }),
                    'contenidoArticulo': forms.TextInput(attrs={'class': 'form-control' }), 
                    'tituloArticulo' : forms.TextInput(attrs={'class': 'form-control' }),
                    } 
    
"""