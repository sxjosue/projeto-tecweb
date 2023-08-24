from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Polo_Amazontech.urls")), #define a rota quando deixar assim a página index inicial é home 
]
