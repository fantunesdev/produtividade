from rest_framework import serializers
from atividades.models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['nome', 'descricao', 'usuario']
