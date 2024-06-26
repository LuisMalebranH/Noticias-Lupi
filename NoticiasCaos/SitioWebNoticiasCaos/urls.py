#from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

from .views import PaginaPrincipal, DetalleNoticia, AgregarArticulo, EditarArticulo




urlpatterns = [
    path('index', views.index, name='index'),
    path('', PaginaPrincipal.as_view(), name='indexprueba'),
    path('noticia/<int:pk>', DetalleNoticia.as_view(), name='pagina_noticia'),
    path('noticia/editar/<int:pk>', EditarArticulo.as_view(), name='editararticulo'),
    path('contacto/', views.contacto, name='contacto'),
    path('suscripcion/', views.suscripcion, name='suscripcion'),
    path('login/', views.login, name='login'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('contacto-laboral/', views.contacto_laboral, name='contacto_laboral'),
    path('agregarnoticia/', AgregarArticulo.as_view(), name='agregarnoticia'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)