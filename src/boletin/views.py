from django.shortcuts import render
from .forms import RegistradoForm
from .models import Registrado


# Create your views here.

def inicio(request):
    titulo = "Bienvenidos"
    form = RegistradoForm(request.POST or None) #sin validaciones
    if form.is_valid():
        instance = form.save(commit=False)#antes de guardar muestro el email hacemos cosas ese comit es no guardarlo
        form.save()
        print instance.email
        print instance.timestamp
    context = {
        "titulo_template":titulo,
        "form":form
    }

    return render(request, "inicio.html", context)
