from rest_framework import serializers

from api.serializers.area_serializer import AreaSerializer
from atividades.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    areas = AreaSerializer(many=True, fields=('id', 'nome'))

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'descricao', 'areas', 'usuario']

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
