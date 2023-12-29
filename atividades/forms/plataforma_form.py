from django import forms

from atividades.models import Plataforma, Area


class PlataformaForm(forms.ModelForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Plataforma
        fields = ['nome', 'descricao', 'areas']
