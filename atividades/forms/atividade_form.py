from django import forms
from ..models import Atividade
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        agora = timezone.localtime(timezone.now()).strftime('%Y-%m-%d')

        fields = ['data', 'area', 'sub_area', 'plataforma', 'pessoa', 'descricao', 'detalhamento', 'tempo']
        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'value': agora})
        }


class AtividadeBuscar(forms.ModelForm):
    class Meta:
        model = Atividade

        fields = ['detalhamento']


class AtividadeFormVer(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['data', 'area', 'sub_area', 'plataforma', 'pessoa', 'descricao', 'detalhamento', 'tempo']
        widgets = {
            'data': forms.TextInput(attrs={'readonly': 'true'}),
            'area': forms.TextInput(attrs={'readonly': 'true'}),
            'sub_area': forms.TextInput(attrs={'readonly': 'true'}),
            'plataforma': forms.TextInput(attrs={'readonly': 'true'}),
            'pessoa': forms.TextInput(attrs={'readonly': 'true'}),
            'descricao': forms.TextInput(attrs={'readonly': 'true'}),
            'detalhamento': forms.TextInput(attrs={'readonly': 'true'}),
            'tempo': forms.TextInput(attrs={'readonly': 'true'}),
        }
