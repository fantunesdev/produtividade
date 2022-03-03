from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import atividade_serializer
from api.services import atividade_service


class AtividadesList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        atividades = atividade_service.listar_semana_atual(request.user)
        serializer = atividade_serializer.AtividadeSerializer(atividades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
