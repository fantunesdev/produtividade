from atividades.models import Atividade
from datetime import date


def listar_semana_atual(usuario):
    semana = date.today().isocalendar()[1]
    atividades = Atividade.objects.prefetch_related('area', 'subarea').filter(data__week=semana,
                                                                              data__year=date.today().year,
                                                                              usuario=usuario)
    return atividades
