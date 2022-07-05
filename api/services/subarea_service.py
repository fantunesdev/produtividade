from atividades.models import SubArea


def listar_subareas_area(usuario, area):
    return SubArea.objects.prefetch_related('areas').filter(usuario=usuario, areas=area)


def editar_subarea(subarea, subarea_nova):
    subarea.nome = subarea_nova.nome
    subarea.descricao = subarea_nova.descricao
    subarea.usuario = subarea_nova.usuario
    subarea.areas.set(subarea_nova.areas)
    subarea.save(force_update=True)
