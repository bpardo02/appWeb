from django.shortcuts import render, get_object_or_404
from .models import Inmueble


def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, "lista_inmuebles.html", {"inmuebles": inmuebles})


def detalle_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    return render(request, "detalle_inmueble.html", {"inmueble": inmueble})


def index(request):
    return render(request, "index.html")
