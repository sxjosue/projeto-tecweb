from django import forms
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'consumo', 'protocolo']