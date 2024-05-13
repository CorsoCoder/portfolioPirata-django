
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ilustracion
from .forms import IlustracionForm
from .models import Categoria
from .forms import CategoriaForm




def ilustracion_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    ilustracion = Ilustracion.objects.filter(Categoria=categoria)
    return render(request, 'ilustracion_por_Categoria.html', {'ilustracion': ilustracion, 'categoria': categoria})

def buscar_por_titulo(request):
    if 'nombre_ilustracion' in request.GET:
        nombre_ilustracion_query = request.GET['nombre_ilustracion']
        # Buscar las ilustraciones que contienen el nombre especificado
        ilustraciones = Ilustracion.objects.filter(titulo__icontains=nombre_ilustracion_query)
    else:
        ilustraciones = Ilustracion.objects.all()

    return render(request, 'galeria.html', {'ilustraciones': ilustraciones})


def galeria(request):
    ilustraciones = Ilustracion.objects.all()
    print(ilustraciones)
    categoria = Categoria.objects.all()
    return render(request, 'galeria.html', {'ilustraciones': ilustraciones,'categoria':categoria})


def listar_categoria(request):
    categoria = Categoria.objects.all()
    return render(request, 'CRUD_categoria/listar_Categoria.html', {'categoria': categoria})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'CRUD_categoria/crear_Categoria.html', {'form': form})

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'CRUD_categoria/editar_Categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        Categoria.delete()
        return redirect('listar_Categoria')
    return render(request, 'CRUD_categoria/eliminar_Categoria.html', {'categoria': categoria})


@login_required
def crear_ilustracion(request):
    if request.method == 'POST':
        form = IlustracionForm(request.POST, request.FILES)
        if form.is_valid():
            ilustracion_instance = form.save(commit=False)  # Guarda la instancia de Ilustracion sin guardar en la base de datos aún
            ilustracion_instance.save()  # Guarda la instancia de Ilustracion en la base de datos

            # Guarda las imágenes asociadas a la ilustración
            for imagen in request.FILES.getlist('imagenes'):
                ilustracion_instance.imagenes.create(imagen=imagen)

            form.save_m2m()  # Guarda las relaciones ManyToMany
            return redirect('galeria')
    else:
        form = IlustracionForm()
    return render(request, 'CRUD_ilustracion/crear_ilustracion.html', {'form': form})
@login_required
def editar_ilustracion(request, slug):
    ilustracion = get_object_or_404(Ilustracion, slug=slug)
    if request.method == 'POST':
        form = IlustracionForm(request.POST, request.FILES, instance=ilustracion)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    else:
        form = IlustracionForm(instance=ilustracion)
    return render(request, 'CRUD_ilustracion/editar_ilustracion.html', {'form': form})

@login_required
def eliminar_ilustracion(request, slug):
    ilustracion = get_object_or_404(Ilustracion, slug=slug)
    if request.method == 'POST':
        ilustracion.delete()
        return redirect('galeria')
    return render(request, 'CRUD_ilustracion/eliminar_ilustracion.html', {'ilustracion': ilustracion})

@login_required
def lista_ilustracion(request):
    ilustracion = Ilustracion.objects.all()
    return render(request, 'CRUD_ilustracion/lista_ilustracion.html', {'ilustracion': ilustracion})






def detalle_ilustracion(request, slug):
    ilustracion = get_object_or_404(Ilustracion, slug=slug)
    return render(request, 'CRUD_ilustracion/detalle_ilustracion.html', {'ilustracion': ilustracion})

def inicio(request):
    return render(request, 'inicio.html')  # Reemplaza 'inicio.html' con la plantilla adecuada para la página de inicio

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')  # Reemplaza 'sobre_nosotros.html' con la plantilla adecuada para la página "Sobre nosotros"

def servicios(request):
    return render(request, 'servicios.html')  # Reemplaza 'servicios.html' con la plantilla adecuada para la página de servicios

def contacto(request):
    return render(request, 'contacto.html')  # Reemplaza 'contacto.html' con la plantilla adecuada para la página de contacto
