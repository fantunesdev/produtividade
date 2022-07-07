from atividades.models import Pessoa


def listar_pessoa_area(usuario, area):
    return Pessoa.objects.prefetch_related('areas').filter(usuario=usuario, areas=area)


def editar_pessoa(pessoa, pessoa_nova):
    pessoa.nome = pessoa_nova.nome
    pessoa.descricao = pessoa_nova.descricao
    pessoa.usuario = pessoa_nova.usuario
    pessoa.save(force_update=True)
    for area in pessoa_nova.areas:
        pessoa.areas.add(area)
    return pessoa
