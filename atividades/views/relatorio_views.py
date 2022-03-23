import json

from django.shortcuts import render

from atividades.encoder import atividade_encoder
from atividades.services import atividade_service
from atividades.views.atividade_views import template_tags


def relatorio(request):
    atividades = atividade_service.listar_ano(request.user, template_tags['ano'])
    json_atividades = atividade_encoder(atividades)
    template_tags['json_atividades'] = json_atividades
    return render(request, 'relatorio/relatorio.html', template_tags)
