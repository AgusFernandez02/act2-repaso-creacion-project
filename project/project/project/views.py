""" 
Actividad 2: 

1. La primera deberá enviar por HttpResponse un string que indique en qué año aproximadamente nació una persona si le pasamos por la url la edad (para revisar si un string es solo numérico se puede usar el método .isnumeric() de los strings que devuelve True en caso de que sean solo números).
"""
from django.http import HttpResponse
from datetime import datetime

def date_of_birth(request, edad: int):
    if edad.isnumeric() == False:
        return HttpResponse("No se paso por la url un valor correcto. Debe pasar un valor entero")
    else:
        año_actual = datetime.now().year
        año_de_nacimiento = año_actual - int(edad)
        return HttpResponse(f"Aproximadamente la persona con edad {edad} nacio en {año_de_nacimiento}")