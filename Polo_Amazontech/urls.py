from django.urls import path
from . import views
#from Polo_Amazontech.views import produtos, cadastro

urlpatterns = [
    path('', views.index, name='index'),
    path("produtos/", views.produtos, name='produtos'),
    path("cadastro/", views.cadastro, name='cadastro')
]