from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Ilustracion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categorias = models.ManyToManyField(Categoria)
    imagenes = models.ManyToManyField('Imagen', related_name='ilustraciones', blank=True)
    es_tatuaje = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Ilustración"
        verbose_name_plural = "Ilustraciones"

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='ilustraciones')

    def __str__(self):
        return f"Imagen #{self.id}"
