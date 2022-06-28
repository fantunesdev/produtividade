from ..models import Plataforma


def cadastrar_plataforma(plataforma):
    nova_plataforma = Plataforma.objects.create(
        nome=plataforma.nome,
        descricao=plataforma.descricao,
        usuario=plataforma.usuario
    )
    nova_plataforma.save()
    for i in plataforma.areas:
        nova_plataforma.areas.set(i)
    return nova_plataforma


def listar_plataformas(usuario):
    plataformas = Plataforma.objects.filter(usuario=usuario)
    return plataformas


def listar_plataforma_id(id, usuario):
    plataforma = Plataforma.objects.filter(id=id, usuario=usuario).first()
    return plataforma


def listar_plataforma_nome(nome, usuario):
    plataforma = Plataforma.objects.get(nome=nome, usuario=usuario).first()
    return plataforma


def editar_plataforma(plataforma, plataforma_nova):
    plataforma.nome = plataforma_nova.nome
    plataforma.descricao = plataforma_nova.descricao
    plataforma.usuario = plataforma_nova.usuario
    for area in plataforma_nova.areas:
        plataforma.areas.set(area)
    plataforma.save(force_update=True)
    return plataforma


def remover_plataforma(plataforma):
    plataforma.delete()
