from django.shortcuts import render
from .models import Usuarios
from django.http import HttpResponse

# Create your views here.

def crear_usuario(request):
    return render(request, "registro.html")

def inicio_app(request):
    return render(request, "inicioapp.html")







