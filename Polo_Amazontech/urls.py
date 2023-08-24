from django.urls import path
from . import views
#from Polo_Amazontech.views import produtos, cadastro

urlpatterns = [
    path('', views.index, name='index'),
    path("produtos.html/", views.produtos, name='produtos'),
    path("cadastro.html/", views.cadastro, name='cadastro')
]