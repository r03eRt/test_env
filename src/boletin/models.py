from __future__ import unicode_literals

from django.db import models

# Create your models here.

#modelo que representa una tabla dentro de la base de datos
class Registrado(models.Model):
    nombre =  models.CharField(max_length=255, blank=True, null=True) #con blank y null eviatmos que no se metan y nos obloga a meterlo
    email = models.EmailField()
    codigo_postal = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    actualizado = models. DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #python 3 __str__
        return self.email