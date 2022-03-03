from atividades.models import SubArea


def listar_sub_area_area(usuario, area):
    return SubArea.objects.prefetch_related('areas').filter(usuario=usuario, areas=area)
