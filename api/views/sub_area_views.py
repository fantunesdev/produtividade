from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import sub_area_serializer
from api.services import sub_area_service as sub_area_service_api
from atividades.entidades.subarea import SubArea
from atividades.services import subarea_service


class SubAreaList(APIView):
    def get(self, request):
        sub_areas = sub_area_service.listar_sub_areas(request.user)
        serializer = sub_area_serializer.SubAreaSerializer(sub_areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = sub_area_serializer.SubAreaSerializer(data=request.data)
        if serializer.is_valid():
            nova_sub_area = SubArea(nome=serializer.validated_data['nome'],
                                    descricao=serializer.validated_data['descricao'],
                                    areas=serializer.validated_data['areas'],
                                    usuario=request.user)
            sub_area_service.cadastrar_sub_area(nova_sub_area)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SubAreaDetalhes(APIView):
    def get(self, request, sub_area_id):
        sub_area = sub_area_service.listar_sub_area_id(request.user, sub_area_id)
        serializer = sub_area_serializer.SubAreaSerializer(sub_area)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, sub_area_id):
        sub_area_antiga = sub_area_service.listar_sub_area_id(request.user, sub_area_id)
        serializer = sub_area_serializer.SubAreaSerializer(sub_area_antiga, data=request.data)
        if serializer.is_valid():
            nova_sub_area = SubArea(nome=serializer.validated_data['nome'],
                                    descricao=serializer.validated_data['descricao'],
                                    areas=serializer.validated_data['areas'],
                                    usuario=request.user)
            sub_area_service_api.editar_sub_area(sub_area_antiga, nova_sub_area)
            return Response(data=request.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, sub_area_id):
        sub_area = sub_area_service.listar_sub_area_id(request.user, sub_area_id)
        sub_area_service.remover_sub_area(sub_area)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubAreaArea(APIView):
    def get(self, request, area_id):
        sub_areas = sub_area_service_api.listar_sub_area_area(request.user, area_id)
        serializer = sub_area_serializer.SubAreaSerializer(sub_areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
