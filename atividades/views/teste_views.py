from django.shortcuts import render

from atividades.views.atividade_views import template_tags
from atividades.repositorios.teste_repositorio import *


def teste(request):
    return render(request, 'teste.html', template_tags)

