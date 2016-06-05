from django.shortcuts import render
from .forms import RegistradoForm
from .models import Registrado


# Create your views here.

def inicio(request):
    titulo = "Bienvenidos"
    form = RegistradoForm(request.POST or None, request.FILES or None) #sin validaciones

    context = {
        "titulo": titulo,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)#antes de guardar muestro el email hacemos cosas ese comit es no guardarlo
        nombre = form.cleaned_data.get("nombre")#cojo el nombre anterior
        form.save()
        context = {
            "titulo":"Gracias por tu registro %s" %(nombre) #cojo el nombre anterir y lo muestro si todo ok
        }
        if not nombre:
            email = form.cleaned_data.get("email")
            context = {
                "titulo": "Gracias %s, ya se ha registrado" %(email)
            }


    return render(request, "inicio.html", context)



def sobre(request):
    titulo = "Sobre Nosotros"

    context = {
        "titulo": titulo,
    }

    return render(request, "sobre-nosotros.html", context)