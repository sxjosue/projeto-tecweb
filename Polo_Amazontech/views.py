from django.shortcuts import render
from .form import ProdutoForm
from .models import Produto #esse ponto indica que o models.py está no mesmo diretorio

def index(request):
    return render(request, 'index.html')

def produtos(request):
    data = {}
    data['Produtos'] = Produto.objects.all() #mostra os objetos que já tem no banco
    return render(request, 'produtos.html', data)

def cadastro(request):
    data = {}
    form = ProdutoForm()
    data['form'] = form
    return render(request, 'cadastro.html', form)