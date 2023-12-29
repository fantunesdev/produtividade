from django import forms
from django.forms import TextInput
from ..models import Area


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome', 'descricao', 'cor']
        widgets = {
            'cor': TextInput(attrs={'type': 'color', 'class': 'form-control'})
        }
