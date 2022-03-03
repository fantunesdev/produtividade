from atividades.models import SubArea


def listar_sub_area_area(usuario, area):
    return SubArea.objects.prefetch_related('areas').filter(usuario=usuario, areas=area)


def editar_sub_area(sub_area, sub_area_nova):
    sub_area.nome = sub_area_nova.nome
    sub_area.descricao = sub_area_nova.descricao
    sub_area.usuario = sub_area_nova.usuario
    sub_area.areas.set(sub_area_nova.areas)
    sub_area.save(force_update=True)
