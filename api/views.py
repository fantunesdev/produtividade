from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.services import atividade_service
from api.serializers import atividade_serializer
from django.contrib.auth.decorators import login_required

# Create your views here.


class AtividadesList(APIView):
    # def get(self, request, format=None):
    #     if request.user.is_authenticated:
    #         usuario_id = request.user.id
    #         atividades = atividade_service.listar_semana_atual(usuario_id)
    #         serializer = atividade_serializer.AtividadeSerializer(atividades, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_403_FORBIDDEN)

    def get(self, request, format=None):
        usuario_id = request.user.id
        atividades = atividade_service.listar_semana_atual(usuario_id)
        serializer = atividade_serializer.AtividadeSerializer(atividades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

