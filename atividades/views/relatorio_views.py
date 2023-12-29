from django.shortcuts import render

from atividades.views.atividade_views import template_tags


def relatorios(request):
    return render(request, 'relatorio/relatorio.html', template_tags)
