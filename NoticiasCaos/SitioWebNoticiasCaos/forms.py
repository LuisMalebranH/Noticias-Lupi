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
                    'fechaPublicacion', 
                    'usuarioAutor'} 

        widgets = { 'tituloArticulo' : forms.TextInput(attrs={'class': 'form-control' }),
                    'contenidoArticulo': forms.TextInput(attrs={'class': 'form-control' }), 
                    'sinopsisArticulo': forms.TextInput(attrs={'class': 'form-control' }),
                    'imagenArticulo': forms.TextInput(attrs={'class': 'form-control' }),
                    'fechaPublicacion': forms.TextInput(attrs={'class': 'form-control' }),
                    'usuarioAutor': forms.TextInput(attrs={'class': 'form-control' })}

    
