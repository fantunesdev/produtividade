from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import pessoa_serializer
from api.services import pessoa_service as pessoa_service_api
from atividades.entidades.pessoa import Pessoa
from atividades.services import pessoa_service


class PessoaList(APIView):
    def post(self, request):
        serializer = pessoa_serializer.PessoaSerializer(data=request.data)
        if serializer.is_valid():
            nova_pessoa = Pessoa(
                nome=serializer.validated_data['nome'],
                descricao=serializer.validated_data['descricao'],
                areas=serializer.validated_data['areas'],
                usuario=request.user
            )
            pessoa_service.cadastrar_pessoa(nova_pessoa)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PessoaDetalhes(APIView):
    def get(self, request, pessoa_id):
        pessoa = pessoa_service.listar_pessoa_id(pessoa_id, request.user)
        serializer = pessoa_serializer.PessoaSerializer(pessoa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pessoa_id):
        pessoa_antiga = pessoa_service.listar_pessoa_id(pessoa_id, request.user)
        serializer = pessoa_serializer.PessoaSerializer(pessoa_antiga, data=request.data)
        if serializer.is_valid():
            pessoa_nova = Pessoa(
                nome=serializer.validated_data['nome'],
                descricao=serializer.validated_data['descricao'],
                areas=serializer.validated_data['areas'],
                usuario=request.user
            )
            pessoa_service_api.editar_pessoa(pessoa_antiga, pessoa_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PessoaArea(APIView):
    def get(self, request, area_id):
        pessoas = pessoa_service_api.listar_pessoa_area(request.user, area_id)
        serializer = pessoa_serializer.PessoaSerializer(pessoas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
