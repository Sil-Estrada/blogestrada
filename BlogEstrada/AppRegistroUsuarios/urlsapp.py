from django.urls import path
from .views import *

urlpatterns = [
    path('usuario/', crear_usuario, name = "registro"),
    path('inicio/', inicio_app, name = "inicio"),
    
    

    




]


