from atividades.services import area_service
from ..utils import tempo_area
from datetime import date


def tempo_atividade(inicio, fim):
    resto = (fim - inicio).total_seconds() % 60
    tempo = int((fim - inicio).total_seconds() // 60)
    if resto <= 10:
        tempo = tempo + 1
    return tempo

def calcular_tempo_atividade_area(atividades):
    areas = area_service.listar_areas()
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