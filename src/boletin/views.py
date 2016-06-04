from django.shortcuts import render
from .models import Registrado


# Create your views here.

def inicio(request):
    titulo = "Bienvenidos"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s!" %(request.user)
    context = {
        "titulo_template": titulo
    }

    return render(request, "inicio.html", context)
