from .area_service import listar_area_id
from ..models import SubArea


def cadastrar_sub_area(sub_area):
    sub_area_banco = listar_sub_area_cadastrada(sub_area)
    if not sub_area_banco:
        sub_area_db = SubArea.objects.create(nome=sub_area.nome,
                                             descricao=sub_area.descricao,
                                             usuario=sub_area.usuario)
        sub_area_db.save()
        sub_area_db.areas.add(sub_area.areas)


def listar_sub_areas(usuario):
    return SubArea.objects.filter(usuario=usuario)


def listar_sub_area_id(usuario, id):
    return SubArea.objects.get(usuario=usuario, id=id)


def listar_sub_area_cadastrada(sub_area):
    return SubArea.objects.prefetch_related('areas').filter(nome=sub_area.nome, areas=sub_area.areas).first()


def listar_sub_area_nome(usuario, nome):
    return SubArea.objects.get(usuario=usuario, nome=nome)


def editar_sub_area(sub_area, sub_area_nova):
    sub_area.nome = sub_area_nova.nome
    sub_area.descricao = sub_area_nova.descricao
    sub_area.areas.set(sub_area_nova.areas)
    sub_area.usuario = sub_area_nova.usuario
    sub_area.save(force_update=True)


def remover_sub_area(sub_area):
    sub_area.delete()
