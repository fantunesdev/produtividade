from rest_framework import serializers
from atividades.models import Atividade

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ('data', 'area', 'sub_area', 'plataforma', 'pessoa', 'descricao', 'tempo', 'usuario')