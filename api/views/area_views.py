from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import area_serializer
from atividades.entidades.area import Area
from atividades.services import area_service


class AreaList(APIView):
    def get(self, request):
        areas = area_service.listar_areas(request.user)
        serializer = area_serializer.AreaSerializer(areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = area_serializer.AreaSerializer(data=request.data)
        if serializer.is_valid():
            nova_area = Area(
                nome=serializer.validated_data['nome'],
                descricao=serializer.validated_data['descricao'],
                cor=serializer.validated_data['cor'],
                usuario=request.user)
            area_service.cadastrar_area(nova_area
                                        )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AreaDetalhes(APIView):
    def get(self, request, area_id):
        area = area_service.listar_area_id(area_id, request.user)
        serializer = area_serializer.AreaSerializer(area)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, area_id):
        area_antiga = area_service.listar_area_id(area_id, request.user)
        serializer = area_serializer.AreaSerializer(area_antiga, data=request.data)
        if serializer.is_valid():
            nova_area = Area(
                nome=serializer.validated_data['nome'],
                descricao=serializer.validated_data['descricao'],
                cor=serializer.validated_data['cor'],
                usuario=request.user
            )
            area_service.editar_area(area_antiga, nova_area)
            return Response(data=request.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, area_id):
        area = area_service.listar_area_id(area_id, request.user)
        area_service.remover_area(area)
        return Response(status=status.HTTP_204_NO_CONTENT)
