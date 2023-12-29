from django import forms

from atividades.models import Pessoa, Area


class PessoaForm(forms.ModelForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Pessoa
        fields = ['nome', 'descricao', 'areas']
