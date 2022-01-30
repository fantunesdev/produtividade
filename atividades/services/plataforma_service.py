from ..models import Plataforma


def cadastrar_plataforma(plataforma):
    Plataforma.objects.create(nome=plataforma.nome, descricao=plataforma.descricao)


def listar_plataformas():
    plataformas = Plataforma.objects.all()
    return plataformas


def listar_plataforma_id(id):
    plataforma = Plataforma.objects.get(id=id)
    return plataforma


def listar_plataforma_nome(nome):
    plataforma = Plataforma.objects.get(nome=nome)
    return plataforma


def editar_plataforma(plataforma, plataforma_nova):
    plataforma.nome = plataforma_nova.nome
    plataforma.descricao = plataforma_nova.descricao
    plataforma.save(force_update=True)


def remover_plataforma(plataforma):
    plataforma.delete()
