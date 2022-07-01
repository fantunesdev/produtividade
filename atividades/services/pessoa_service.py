from atividades.models import Pessoa


def cadastrar_pessoa(pessoa):
    nova_pessoa = Pessoa.objects.create(
        nome=pessoa.nome,
        descricao=pessoa.descricao,
        usuario=pessoa.usuario
    )
    nova_pessoa.save()
    # for i in pessoa.areas:
    #     nova_pessoa.areas.set(i)
    return nova_pessoa


def listar_pessoas(usuario):
    return Pessoa.objects.filter(usuario=usuario)


def listar_pessoa_id(id, usuario):
    return Pessoa.objects.filter(id=id, usuario=usuario).first()


def listar_pessoa_nome(nome, usuario):
    return Pessoa.objects.get(nome=nome, usuario=usuario)


def editar_pessoa(pessoa, pessoa_nova):
    pessoa.nome = pessoa_nova.nome
    pessoa.descricao = pessoa_nova.descricao
    pessoa.usuario = pessoa_nova.usuario
    pessoa.save(force_update=True)
    for area in pessoa_nova.areas:
        pessoa.areas.set(area)
    return pessoa


def remover_pessoa(pessoa):
    pessoa.delete()
