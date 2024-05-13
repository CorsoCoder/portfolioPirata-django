from django.contrib import admin
from .models import Ilustracion, Categoria

# Register your models here.

@admin.register(Ilustracion)
class IlustracionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'es_tatuaje')
    list_filter = ('es_tatuaje', 'categorias')
    search_fields = ('titulo', 'descripcion')
    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


