#from django.conf.urls import url
from django.urls import path
from . import views
from .views import PaginaPrincipal, DetalleNoticia, AgregarArticulo



urlpatterns = [
    path('index', views.index, name='index'),
    path('', PaginaPrincipal.as_view(), name='indexprueba'),
    path('noticia/<int:pk>', DetalleNoticia.as_view(), name='pagina_noticia'),
    path('agregarnoticia/', AgregarArticulo.as_view(), name='agregarnoticia'),

]