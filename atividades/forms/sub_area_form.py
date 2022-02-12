from django import forms
from ..models import SubArea, Area


class SubAreaForm(forms.ModelForm):
    areas = forms.ModelChoiceField(queryset=Area.objects.all())

    class Meta:
        model = SubArea
        fields = ['nome', 'descricao', 'areas']
