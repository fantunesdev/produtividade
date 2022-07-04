from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import subarea_serializer
from api.services import subarea_service as subarea_service_api
from atividades.entidades.subarea import SubArea
from atividades.services import subarea_service


class SubAreaList(APIView):
    def get(self, request):
        subareas = subarea_service.listar_subareas(request.user)
        serializer = subarea_serializer.SubAreaSerializer(subareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = subarea_serializer.SubAreaSerializer(data=request.data)
        if serializer.is_valid():
            nova_subarea = SubArea(
                nome=serializer.validated_data['nome'],
                descricao=serializer.validated_data['descricao'],
                areas=serializer.validated_data['areas'],
                usuario=request.user
            )
            subarea_service.cadastrar_subarea(nova_subarea)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SubAreaDetalhes(APIView):
    def get(self, request, subarea_id):
        subarea = subarea_service.listar_subarea_id(request.user, subarea_id)
        serializer = subarea_serializer.SubAreaSerializer(subarea)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, subarea_id):
        subarea_antiga = subarea_service.listar_subarea_id(request.user, subarea_id)
        serializer = subarea_serializer.SubAreaSerializer(subarea_antiga, data=request.data)
        if serializer.is_valid():
            nova_subarea = SubArea(
                nome=serializer.validated_data['nome'],
                descricao=serializer.validated_data['descricao'],
                areas=serializer.validated_data['areas'],
                usuario=request.user
            )
            subarea_service_api.editar_subarea(subarea_antiga, nova_subarea)
            return Response(data=request.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subarea_id):
        subarea = subarea_service.listar_subarea_id(request.user, subarea_id)
        subarea_service.remover_subarea(subarea)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubAreaArea(APIView):
    def get(self, request, area_id):
        subareas = subarea_service_api.listar_subarea_area(request.user, area_id)
        serializer = subarea_serializer.SubAreaSerializer(subareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
