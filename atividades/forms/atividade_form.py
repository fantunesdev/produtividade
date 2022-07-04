from django import forms
from ..models import Atividade
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        agora = timezone.localtime(timezone.now()).strftime('%Y-%m-%d')

        fields = ['data', 'area', 'subarea', 'plataforma', 'pessoa', 'descricao', 'detalhamento', 'tempo']
        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'value': agora})
        }


class AtividadeBuscar(forms.ModelForm):
    class Meta:
        model = Atividade

        fields = ['detalhamento']
        widgets = {
            'detalhamento': forms.DateInput(attrs={'class': 'form-control'})
        }
