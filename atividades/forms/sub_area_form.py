from django import forms
from ..models import SubArea, Area


class SubAreaForm(forms.ModelForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = SubArea
        fields = ['nome', 'descricao', 'areas']
