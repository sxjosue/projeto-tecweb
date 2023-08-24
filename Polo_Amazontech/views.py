from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def produtos(request):
    return(render, 'produtos.html')