from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import pessoa_serializer
from api.services import pessoa_service


class PessoaArea(APIView):
    def get(self, request, area_id):
        pessoas = pessoa_service.listar_pessoa_area(request.user, area_id)
        serializer = pessoa_serializer.PessoaSerializer(pessoas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
