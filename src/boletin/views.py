from django.shortcuts import render
# para utiliar el formulario tengo que importarlo
from .forms import  RegistradoForm
#metemos este modelo a qwui porque vamos a ir guardando los datos en el modelo
from .models import Registrado


# Create your views here.

def inicio(request):
    form = RegistradoForm(request.POST or None)  # con request.POST pillamos el formulario post de la pagina, con or none no hacemmos que salga mensaje de error antes
    context = {
        "form":form
    }

    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("nombre_form") #cojo del pormulario el nombre
        obj = Registrado.objects.create(nombre=abc) #1a forma de anadir en la base de datos con esto creamos un modelo con el nombre registrado pero tenemos que ver que todos los campos que no peuden ser null esten

    return render(request, "inicio.html", context)
