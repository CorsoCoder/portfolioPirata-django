# forms.py
from django import forms
from .models import Ilustracion
from .models import Categoria
from django.forms import ClearableFileInput

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result if result is not None else []



class IlustracionForm(forms.ModelForm):
    imagenes  = MultipleFileField(label='Select files', required=False)

    class Meta:
        model = Ilustracion
        fields = ['titulo', 'descripcion', 'categorias', 'es_tatuaje']
        


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']