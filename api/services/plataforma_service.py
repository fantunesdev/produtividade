from atividades.models import Plataforma


def listar_plataforma_area(usuario, area):
    return Plataforma.objects.prefetch_related('areas').filter(usuario=usuario, areas=area)
