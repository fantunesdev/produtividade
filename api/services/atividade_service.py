from atividades.models import Atividade
from datetime import date

def listar_semana_atual(usuario_id):
    semana = date.today().isocalendar()[1]
    atividades = Atividade.objects.filter(usuario=usuario_id, data__week=semana, data__year=2021)
    return atividades