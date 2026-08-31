from django import forms
from home.models import Pintura


class PinturaForm(forms.ModelForm):

    class Meta:
        model = Pintura
        fields = ("nro_pintura","nombre", "autor", "descripcion")