from django import forms
from django.core.exceptions import ValidationError

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
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control-data' , 'type': 'date', 'value': agora})
        }

    def clean_area(self):
        area = self.cleaned_data['area']
        if area == 0:
            raise ValidationError('Selecione um item da lista.')
        else:
            return area

    def clean_subarea(self):
        subarea = self.cleaned_data['subarea']
        if subarea == 0:
            raise ValidationError('Selecione um item da lista.')
        else:
            return subarea

    def clean_plataforma(self):
        plataforma = self.cleaned_data['plataforma']
        if plataforma == 0:
            raise ValidationError('Selecione um item da lista.')
        else:
            return plataforma

    def clean_pessoa(self):
        pessoa = self.cleaned_data['pessoa']
        if pessoa == 0:
            raise ValidationError('Selecione um item da lista.')
        else:
            return pessoa
        

class AtividadeEmLoteForm(AtividadeForm):

    agora = timezone.localtime(timezone.now()).strftime('%Y-%m-%d')
    
    data_final = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date', 'class': 'form-control', 'value': agora})
        )
    
    dias_da_semana = forms.MultipleChoiceField(
        choices=(
            (0, 'Seg'),
            (1, 'Ter'),
            (2, 'Qua'),
            (3, 'Qui'),
            (4, 'Sex'),
            (5, 'Sab'),
            (6, 'Dom'),
        ),
        widget=forms.CheckboxSelectMultiple()
    )

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        data_final = cleaned_data.get('data_final')

        if data and data_final and data_final < data:
            self.add_error('data_final', 'A data final deve ser maior ou igual à data inicial.')

        return cleaned_data

    



class AtividadeBuscar(forms.ModelForm):
    class Meta:
        model = Atividade

        fields = ['detalhamento']
        widgets = {
            'detalhamento': forms.DateInput(attrs={'class': 'form-control'})
        }
