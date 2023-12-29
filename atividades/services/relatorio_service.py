from atividades.models import Atividade


def listar_atividades_ano(ano, usuario):
    return Atividade.objects.annotate()
