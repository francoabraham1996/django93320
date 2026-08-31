from django.shortcuts import render, get_object_or_404, redirect
from home.models import Pintura
from home.forms import PinturaForm

def home(request):
    return render(request, "home/home.html")

def listado_de_pinturas(request):
    
    numeros = list(range(16))

    pinturas = Pintura.objects.all()

    nombre = request.GET.get("nombre")

    if nombre is not None:
        pinturas = pinturas.filter(nombre__icontains=nombre)

    return render(
        request,
        "home/Listado_de_pinturas.html",
        {"pinturas": pinturas}
    )


def ver_pintura(request, pk):
    pintura = get_object_or_404(Pintura, pk=pk)

    contexto = {
        "pintura": pintura
    }

    return render(request, "home/ver_pintura.html", contexto)

def crear_pintura(request):

    if request.method == "POST":
        form = PinturaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("listar_pinturas")

    else:
        form = PinturaForm()

    return render(request, "home/crear_pintura.html", {"form": form})


# CRUD
# CREATE
# READ
# UPDATE
# DELATE