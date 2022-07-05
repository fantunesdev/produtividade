from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import plataforma_serializer
from api.services.plataforma_service import listar_plataforma_area


class PlataformaArea(APIView):
    def get(self, request, area_id):
        plataformas = listar_plataforma_area(request.user, area_id)
        serializer = plataforma_serializer.PlataformaSerializer(plataformas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
