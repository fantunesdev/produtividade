from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import plataforma_serializer
from api.services import plataforma_service as plataforma_service_api
from atividades.entidades.plataforma import Plataforma
from atividades.services import plataforma_service


class PlataformaList(APIView):
    def post(self, request):
        serializer = plataforma_serializer.PlataformaSerializer(data=request.data)
        if serializer.is_valid():
            nova_plataforma = Plataforma(
                nome=serializer.validated_data['nome'],
                descricao=serializer.validated_data['descricao'],
                areas=serializer.validated_data['areas'],
                usuario=request.user
            )
            plataforma_service.cadastrar_plataforma(nova_plataforma)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlataformaDetalhes(APIView):
    def get(self, request, plataforma_id):
        plataforma = plataforma_service.listar_plataforma_id(plataforma_id, request.user)
        serializer = plataforma_serializer.PlataformaSerializer(plataforma)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, plataforma_id):
        plataforma_antiga = plataforma_service.listar_plataforma_id(plataforma_id, request.user)
        serializer = plataforma_serializer.PlataformaSerializer(plataforma_antiga, data=request.data)
        if serializer.is_valid():
            nova_plataforma = Plataforma(
                nome=serializer.validated_data['nome'],
                descricao=serializer.validated_data['descricao'],
                areas=serializer.validated_data['areas'],
                usuario=request.user
            )
            plataforma_service_api.editar_plataforma(plataforma_antiga, nova_plataforma)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlataformaArea(APIView):
    def get(self, request, area_id):
        plataformas = plataforma_service_api.listar_plataforma_area(request.user, area_id)
        serializer = plataforma_serializer.PlataformaSerializer(plataformas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
