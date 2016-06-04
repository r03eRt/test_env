from django.shortcuts import render

# para utiliar el formulario tengo que importarlo
from .forms import RegForm

#metemos este modelo a qwui porque vamos a ir guardando los datos en el modelo
from.models import Registrado


# Create your views here.

def inicio(request):
    form = RegForm(
        request.POST or None)  # con request.POST pillamos el formulario post de la pagina, con or none no hacemmos que salga mensaje de error antes
    # diccionario de contexto
    context = {
        "form": form
    }

    if form.is_valid():
        # print form.cleaned_data #con esto envia los datos en formato para imprimir en consola(1)
        #form_dicc = form.cleaned_data
        #print form_dicc.get("nombre")  # con esto coge los datos y los impime por consolaq(2)

        form_data = form.cleaned_data
        abc = form_data.get("nombre_form") #cojo del pormulario el nombre
        obj = Registrado.objects.create(nombre=abc) #1a forma de añadir en la base de datos con esto creamos un modelo con el nombre registrado pero tenemos que ver que todos los campos que no peuden ser null esten

        #2a forma de guardar en BBDD
        #obj2 = Registrado()
        #obj2.nombre = abc
        #obj2.save()
        #fin segunda forma

    return render(request, "inicio.html", context)
