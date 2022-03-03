from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import area_serializer
from atividades.services import area_service


class AreaList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        areas = area_service.listar_areas()
        serializer = area_serializer.AreaSerializer(areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AreaDetalhes(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, area_id):
        area = area_service.listar_area_id(area_id)
        serializer = area_serializer.AreaSerializer(area)
        return Response(serializer.data, status=status.HTTP_200_OK)
