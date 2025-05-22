from django.shortcuts import render
# Se importa el Http
from django.http import HttpResponse
# Create your views here.

#Creamos la función que envía la solictud y responde con el texto
def inicio(request):
    return HttpResponse("<h1>Bienvenido a la Liberia</h1>")
#Creamos la función que busca el archivo nosotros .html
def nosotros(request):
    return render(request, 'paginas/nosotros.html')