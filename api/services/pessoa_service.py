from atividades.models import Pessoa


def listar_pessoa_area(usuario, area):
    return Pessoa.objects.prefetch_related('areas').filter(usuario=usuario, areas=area)
