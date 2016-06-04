from django.contrib import admin

# Register your models here.

from .models import Registrado
class AdminRegistrado(admin.ModelAdmin):
    #
    list_display = ['__unicode__',"nombre", "codigo_postal", "timestamp", "actualizado"]
    class Meta:
        model = Registrado #ponemos el nombre del modelo al que hacemos referencia


#registramos modelo en la vista de admin
admin.site.register(Registrado, AdminRegistrado)