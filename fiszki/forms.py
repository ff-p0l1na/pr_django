from django import forms
from django.forms import ModelForm
from .models import Fiszka


class FormularzDodawniaFiszek(ModelForm):
    class Meta:
        model = Fiszka
        fields = ('przod', 'tyl', 'mnemo')

        widgets = {
            'przod': forms.TextInput(attrs={'class': 'form-control'}),
            'tyl': forms.TextInput(attrs={'class': 'form-control'}),
            'mnemo': forms.TextInput(attrs={'class': 'form-control'}),
        }

