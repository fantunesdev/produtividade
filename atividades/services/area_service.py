from ..models import Area


def cadastrar_area(area):
    Area.objects.create(nome=area.nome,
                        descricao=area.descricao,
                        cor=area.cor,
                        usuario=area.usuario)


def listar_areas(usuario):
    areas = Area.objects.filter(usuario=usuario)
    return areas


def listar_area_id(usuario, id):
    area = Area.objects.filter(usuario=usuario, id=id).first()
    return area


def listar_area(usuario, nome):
    area = Area.objects.filter(usuario=usuario, nome=nome).first()
    return area


def editar_area(area, area_nova):
    area.nome = area_nova.nome
    area.descricao = area_nova.descricao
    area.cor = area_nova.cor
    area.save(force_update=True)


def remover_area(area):
    area.delete()
