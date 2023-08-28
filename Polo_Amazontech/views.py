from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth.decorators import login_required
from .form import ProdutoForm
from .models import Produto #esse ponto indica que o models.py está no mesmo diretorio

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Usuario ja cadastrado")

        user = User.objects.create_user(username=username, email=email, password=senha) #parâmetros para criar o usuario
        user.save()

        return HttpResponse("Usuario cadastrado com sucesso")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            Login(request, user)
            return HttpResponse('Bem vindo!')
        else:
            return HttpResponse('Email ou senha invalidos')

def index(request):
    return render(request, 'index.html')

def produtos(request):
    data = {}
    data['Produtos'] = Produto.objects.all() #mostra os objetos que já tem no banco
    return render(request, 'produtos.html', data)

@login_required(login_url = "login.html/") #não aparecenas views isso aqui
def cadastro(request):
        return render(request, 'cadastro.html') #algumas coisas o usuario so pode acessar com login feito
