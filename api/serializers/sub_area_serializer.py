from rest_framework import serializers

from api.serializers.area_serializer import AreaSerializer
from atividades.models import SubArea


class SubAreaSerializer(serializers.ModelSerializer):
    areas = AreaSerializer(many=True)

    class Meta:
        model = SubArea
        fields = ['id', 'nome', 'descricao', 'areas', 'usuario']
