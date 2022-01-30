from django import forms
from ..models import SubArea


class SubAreaForm(forms.ModelForm):
    class Meta:
        model = SubArea
        fields = ['nome', 'descricao', 'area']
