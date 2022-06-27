from datetime import date

from django.core.exceptions import ObjectDoesNotExist

from atividades.services import area_service, plataforma_service, atividade_service
from ..entidades.atividade import Atividade
from ..entidades.plataforma import Plataforma
from ..utils import tempo_area


def tempo_atividade(inicio, fim):
    resto = (fim - inicio).total_seconds() % 60
    tempo = int((fim - inicio).total_seconds() // 60)
    if resto <= 10:
        tempo = tempo + 1
    return tempo


def calcular_tempo_atividade_area(atividades, usuario):
    areas = area_service.listar_areas(usuario)
    lista_areas = []
    for area in areas:
        cor = to_rgba(area.cor)
        area_tempo = tempo_area.TempoArea(area.nome, 0, cor)
        lista_areas.append(area_tempo)
    for atividade in atividades:
        for area in lista_areas:
            if atividade.area.nome == area.nome:
                area.tempo += atividade.tempo
    tempo_total = tempo_area.TempoArea('Total', 0, None)
    for area in lista_areas:
        tempo_total.tempo += area.tempo
    lista_areas.append(tempo_total)
    return lista_areas


def to_rgba(hex, format_string='rgba({r},{g},{b},0.85)'):
    hex = hex.replace('#', '')
    out = {'r': int(hex[0:2], 16),
           'g': int(hex[2:4], 16),
           'b': int(hex[4:6], 16)}
    return format_string.format(**out)


def criar_dicionario(numero, tipo):
    if tipo == 'y':
        atual = date.today().year
    elif tipo == 'm':
        atual = date.today().month
    elif tipo == 'w':
        atual = date.today().isocalendar()[1]
    else:
        atual = date.today().isocalendar()[1]

    dicionario = {
        '<<': numero - 1,
        'Atual': atual,
        '>>': numero + 1
    }
    return dicionario


# Funções temporárias

class FuncoesTemporarias:
    def cadastrar_plataformas(self, atividades):
        for i in atividades:
            nova_plataforma = Plataforma(
                nome=i.plataforma,
                descricao=None,
                usuario=1,
                areas=1
            )
            try:
                plataforma_db = plataforma_service.listar_plataforma_nome(nova_plataforma.nome)
            except ObjectDoesNotExist:
                plataforma_db = plataforma_service.cadastrar_plataforma(nova_plataforma)

            nova_atividade = Atividade(
                data=i.data,
                area=i.area,
                sub_area=i.sub_area,
                plataforma=plataforma_db.id,
                pessoa=i.pessoa,
                descricao=i.descricao,
                detalhamento=i.detalhamento,
                tempo=i.tempo,
                inicio=i.inicio,
                fim=i.fim,
                usuario=i.usuario
            )
            atividade_service.editar_atividade(i, nova_atividade)
