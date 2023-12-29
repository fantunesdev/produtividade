from ..models import SubArea


def cadastrar_subarea(subarea):
    subarea_db = listar_subarea_nome(subarea.usuario, subarea.nome)
    if subarea_db:
        subarea_relacionada_area = listar_subarea_nome_area_id(subarea.usuario, subarea.nome, subarea.areas)
        if not subarea_relacionada_area:
            for i in subarea.areas:
                subarea_db.areas.add(i)
    else:
        nova_subarea = SubArea.objects.create(nome=subarea.nome,
                                               descricao=subarea.descricao,
                                               usuario=subarea.usuario)
        nova_subarea.save()
        for i in subarea.areas:
            nova_subarea.areas.add(i)
        return nova_subarea


def listar_subareas(usuario):
    subareas = SubArea.objects.filter(usuario=usuario)
    return subareas


def listar_subarea_id(usuario, id):
    return SubArea.objects.get(usuario=usuario, id=id)


def listar_subarea_nome_area_id(usuario, nome, area_id):
    return SubArea.objects.prefetch_related('areas').filter(usuario=usuario, nome=nome, areas=area_id).first()


def listar_subarea_nome(usuario, nome):
    return SubArea.objects.filter(usuario=usuario, nome=nome).first()


def editar_subarea(subarea, subarea_nova):
    subarea.nome = subarea_nova.nome
    subarea.descricao = subarea_nova.descricao
    subarea.usuario = subarea_nova.usuario
    for area in subarea_nova.areas:
        subarea.areas.set(area)
    subarea.save(force_update=True)
    return subarea


def remover_subarea(subarea):
    subarea.delete()
