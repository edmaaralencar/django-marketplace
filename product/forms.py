from django import forms
from .models import Product

INPUT_CLASSES = 'w-full mt-2 px-4 py-2 rounded-xl'

class NewProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ('name', 'description', 'price', 'image')
    labels = {
      'name': 'Nome',
      'description': 'Descrição',
      'price': 'Preço',
      'image': 'Imagem'
    }

    widgets = {
      'name': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'description': forms.Textarea(attrs={
        'class': INPUT_CLASSES
      }),
      'price': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'image': forms.FileInput(attrs={
        'class': INPUT_CLASSES
      }),
    }

class EditProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ('name', 'description', 'price', 'image', 'is_sold')
