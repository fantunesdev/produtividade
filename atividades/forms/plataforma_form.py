from django import forms
from ..models import Plataforma

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nome', 'descricao']