from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Articulo
# Create your views here.

#Aca se crea todo lo que es vista, se puede generar desde un archivo HTML o se
#Pueden usar los templates existentes en Django (ERRORES Y FORMularios de ingreso)


class PaginaPrincipal(ListView):
    model = Articulo
    template_name = 'SitioWebNoticiasCaos/indexprueba.html'

class DetalleNoticia(DetailView):
    model = Articulo
    template_name = 'SitioWebNoticiasCaos/paginanoticia.html'

class AgregarArticulo(CreateView):
    model = Articulo
    template_name = 'SitioWebNoticiasCaos/creararticulo.html'
    fields = ["tituloArticulo", "etiquetaTitulo", "contenidoArticulo", 
             "imagenArticulo", "usuarioAutor"]


def index(request):
    context={}
    return render(request, 'SitioWebNoticiasCaos/index.html', context)

