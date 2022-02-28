from ..models import SubArea


def cadastrar_sub_area(sub_area):
    sub_area_db = listar_sub_area_nome(sub_area.usuario, sub_area.nome)
    if sub_area_db:
        sub_area_relacionada_area = listar_sub_area_nome_area_id(sub_area.usuario, sub_area.nome, sub_area.areas)
        if not sub_area_relacionada_area:
            sub_area_db.areas.add(sub_area.areas)
    else:
        nova_sub_area = SubArea.objects.create(nome=sub_area.nome,
                                               descricao=sub_area.descricao,
                                               usuario=sub_area.usuario)
        nova_sub_area.save()
        nova_sub_area.areas.add(sub_area.areas)


def listar_sub_areas(usuario):
    return SubArea.objects.filter(usuario=usuario)


def listar_sub_area_id(usuario, id):
    return SubArea.objects.get(usuario=usuario, id=id)


def listar_sub_area_nome_area_id(usuario, nome, area_id):
    return SubArea.objects.prefetch_related('areas').filter(usuario=usuario, nome=nome, areas=area_id).first()


def listar_sub_area_nome(usuario, nome):
    return SubArea.objects.filter(usuario=usuario, nome=nome).first()


def editar_sub_area(sub_area, sub_area_nova):
    sub_area.nome = sub_area_nova.nome
    sub_area.descricao = sub_area_nova.descricao
    sub_area.usuario = sub_area_nova.usuario
    for area in sub_area_nova.areas:
        sub_area.areas.set(area)
    sub_area.save(force_update=True)


def remover_sub_area(sub_area):
    sub_area.delete()
