from django.http import HttpResponse
import datetime


def dia_de_hoy (request):
    dia=datetime.datetime.today()
    cadena= f"hoy es {dia}"
    return HttpResponse(cadena)
