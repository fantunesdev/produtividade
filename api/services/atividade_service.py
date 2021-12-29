from atividades.models import Atividade
from datetime import date

def listar_semana_atual(usuario):
    semana = date.today().isocalendar()[1]
    atividades = Atividade.objects.prefetch_related('area').filter(data__week=semana, data__year=2021, usuario=usuario)
    for i in atividades.area:
        print(i.nome)
    return atividades