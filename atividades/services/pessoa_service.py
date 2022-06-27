from atividades.models import Pessoa


def cadastrar_pessoa(pessoa):
    return Pessoa.objects.create(
        nome=pessoa.nome,
        descricao=pessoa.descricao
    )


def listar_pessoa_nome(nome):
    return Pessoa.objects.get(nome=nome)
