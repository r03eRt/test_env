#formulatio de
from django import forms

from .models import Registrado

#formulario para mostra en la vista

class RegistradoForm(forms.ModelForm):
    class Meta:
        #modelo que suamos
        model = Registrado
        #campos que usaremos
        fields = ["nombre","email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio,extension = proveedor.split(".")
        if not extension == "co":
            raise forms.ValidationError("Tienes que introducir correo acabado en .co")
        return email


class RegForm(forms.Form):
    nombre_form = forms.CharField(max_length=100)
    edad = forms.IntegerField()



