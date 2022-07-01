from django.shortcuts import render

from atividades.views.atividade_views import template_tags
from atividades.repositorios.teste_repositorio import *


def teste(request):
    """
    Função que faz a migração dos campos de texto Plataforma e Pessoa para os models Plataforma e Pessoa
    """
    atividades = atividade_service.listar_atividades(request.user)
    template_tags['atividades'] = atividades
    # 1 - Popular as tabelas plataforma e pessoa
    # cadastrar_plataformas(atividades)
    # cadastrar_pessoas(atividades)
    # 2 - Corrigir o erro no banco de dados com o registro 2329
    # update atividades_atividade set pessoa=1 where id=2329;
    # update atividades_atividade set plataforma=15 where id=2329;
    # 3 - Alterar o Models e fazer as migrações
    # 4 - Editar as plataformas e as pessoas
    # relacionar_plataformas(atividades)
    # relacionar_pessoas(atividades)
    # 5 - Remover os comentários dos métodos de cadastro de pessoa e de plataforma
    return render(request, 'teste.html', template_tags)
