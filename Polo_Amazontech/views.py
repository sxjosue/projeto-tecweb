from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
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

        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse("<center>Usuario ja cadastrado</center>")

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
            return render(request, 'produtos.html')
        else:
            return HttpResponse('<center>Usuario ou senha invalidos</center>')
            return redirect('login')

def index(request):
    return render(request, 'index.html')

def produtos(request):
    data = {}
    data['Produtos'] = Produto.objects.all() #mostra os objetos que já tem no banco
    return render(request, 'produtos.html', data)

@login_required(login_url = "login") #foi só remover '/', isso significa que ele indentificou o nome
def cadastro(request):
        return render(request, 'cadastro.html') #algumas coisas o usuario so pode acessar com login feito

def logout(resquest):
    Logout(resquest)
    return redirect('index')
