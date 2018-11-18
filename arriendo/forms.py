from django import forms
from arriendo.models import *
from django.core.exceptions import ValidationError


class ArriendoForm(forms.ModelForm):
    """
    participantes = forms.IntegerField()
    duracion = forms.IntegerField()
    """
    class Meta:
        model = Arriendo
        fields = ['participantes', 'duracion']