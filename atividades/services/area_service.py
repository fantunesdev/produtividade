from ..models import Area


def cadastrar_area(area):
    Area.objects.create(nome=area.nome, descricao=area.descricao)


def listar_areas():
    areas = Area.objects.all()
    return areas


def listar_area_id(id):
    area = Area.objects.get(id=id)
    return area


def listar_area(nome):
    area = Area.objects.get(nome=nome)
    return area


def editar_area(area, area_nova):
    area.nome = area_nova.nome
    area.descricao = area_nova.descricao
    area.save(force_update=True)


def remover_area(area):
    area.delete()
