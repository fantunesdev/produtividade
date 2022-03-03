from rest_framework import serializers
from atividades.models import SubArea


class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = ['nome', 'descricao', 'areas', 'usuario', 'areas']
