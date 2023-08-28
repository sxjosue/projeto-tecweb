from django.urls import path
from . import views
#from Polo_Amazontech.views import produtos, cadastro

urlpatterns = [
    path('', views.index, name='index'),
    path("produtos.html/", views.produtos, name='produtos'),
    path("produtos.html/cadastro.html/", views.cadastro, name='cadastro'), #cadastro de produto
    path("signup.html/", views.signup, name='signup'), #cadastro do usário
    path("login.html/", views.login, name='login'), #login do usuário
]