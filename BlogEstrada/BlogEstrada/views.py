from django.http import HttpResponse
import datetime
from django.shortcuts import render


def dia_de_hoy (request):
    dia=datetime.datetime.today()
    cadena= f"hoy es {dia}"
    return HttpResponse(cadena)

def inicio (request):
    return HttpResponse('pagina de inicio')

#def inicio_(request):
  #  return render(request, "AppRegistroUsuarios/iniapp.html")
