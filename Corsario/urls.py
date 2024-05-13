"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from portfolio.views import *
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  # URL para la página de inicio
    path('galeria/', galeria, name='galeria'),  # URL para la página de galería
    path('ilustracion/<slug:slug>/', views.detalle_ilustracion, name='detalle_ilustracion'),

    path('sobre-nosotros/', sobre_nosotros, name='sobre_nosotros'),  # URL para la página "Sobre nosotros"
    path('servicios/', servicios, name='servicios'),  # URL para la página de servicios
    path('contacto/', contacto, name='contacto'),  # URL para la página de contacto
    
    path('crear/', views.crear_ilustracion, name='crear_ilustracion'),
    path('editar/<slug:slug>/', views.editar_ilustracion, name='editar_ilustracion'),
    path('eliminar/<slug:slug>/', views.eliminar_ilustracion, name='eliminar_ilustracion'),
    path('lista/', views.lista_ilustracion, name='lista_ilustracion'),
    
    path('categorias/', views.listar_categoria, name='listar_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/<int:categoria_id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:categoria_id>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),

    path('buscar/', views.buscar_por_titulo, name='buscar_por_titulo'),

    path('categoria/<int:categoria_id>/', views.ilustracion_por_categoria, name='ilustracion_por_categoria'),

]+ static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)