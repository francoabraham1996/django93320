from django.shortcuts import render
from home.models import Pintura

def home(request):
    return render(request, "home/home.html")

def listado_de_pinturas(request):
    
    numeros = list(range(16))

    pinturas = Pintura.objects.all()


    return render(request, "home/Listado_de_pinturas.html", {'pinturas': pinturas})
