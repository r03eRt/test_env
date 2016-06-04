#formulatio de
from django import forms

class RegForm(forms.Form):
    nombre_form = forms.CharField(max_length=100)
    edad = forms.IntegerField()
