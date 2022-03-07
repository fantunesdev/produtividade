from rest_framework import serializers

from api.serializers.area_serializer import AreaSerializer
from api.serializers.sub_area_serializer import SubAreaSerializer
from atividades.models import Atividade


class AtividadeSerializer(serializers.ModelSerializer):
    area = AreaSerializer(fields=('id', 'nome', 'cor'))
    sub_area = SubAreaSerializer(fields=('id', 'nome', 'areas'))

    class Meta:
        model = Atividade
        fields = ['id', 'data', 'area', 'sub_area', 'plataforma', 'pessoa', 'descricao', 'tempo', 'usuario']
