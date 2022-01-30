from ..models import SubArea


def cadastrar_sub_area(sub_area):
    SubArea.objects.create(nome=sub_area.nome,
                           descricao=sub_area.descricao,
                           area=sub_area.area,
                           usuario=sub_area.usuario)


def listar_sub_areas(usuario):
    return SubArea.objects.filter(usuario=usuario)


def listar_sub_area_id(usuario, id):
    return SubArea.objects.get(usuario=usuario, id=id)


def listar_sub_area_nome(usuario, nome):
    return SubArea.objects.get(usuario=usuario, nome=nome)


def editar_sub_area(sub_area, sub_area_nova):
    sub_area.nome = sub_area_nova.nome
    sub_area.descricao = sub_area_nova.descricao
    sub_area.area = sub_area_nova.area
    sub_area.usuario = sub_area_nova.usuario
    sub_area.save(force_update=True)


def remover_sub_area(sub_area):
    sub_area.delete()
