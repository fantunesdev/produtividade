from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from atividades.entidades.atividade import Atividade
from atividades.entidades.pessoa import Pessoa
from atividades.entidades.plataforma import Plataforma
from atividades.services import plataforma_service, atividade_service, pessoa_service


def cadastrar_plataformas(atividades):
    for i in atividades:
        nova_plataforma = Plataforma(
            nome=i.plataforma,
            descricao=None,
            usuario=i.usuario,
            areas=1
        )
        try:
            plataforma_db = plataforma_service.listar_plataforma_nome(nova_plataforma.nome, nova_plataforma.usuario)
        except ObjectDoesNotExist:
            plataforma_db = plataforma_service.cadastrar_plataforma(nova_plataforma)

        nova_atividade = Atividade(
            data=i.data,
            area=i.area,
            sub_area=i.sub_area,
            plataforma=plataforma_db.id,
            pessoa=i.pessoa,
            descricao=i.descricao,
            detalhamento=i.detalhamento,
            tempo=i.tempo,
            inicio=i.inicio,
            fim=i.fim,
            usuario=i.usuario
        )
        atividade_service.editar_atividade(i, nova_atividade)


def relacionar_plataformas(atividades):
    for atividade in atividades:
        plataforma_db = plataforma_service.listar_plataforma_id(atividade.plataforma.id, atividade.usuario)
        plataforma_db.areas.add(atividade.area)


def relacionar_pessoas(atividades):
    for atividade in atividades:
        pessoa_db = pessoa_service.listar_pessoa_id(atividade.pessoa.id, atividade.usuario)
        pessoa_db.areas.add(atividade.area)


def cadastrar_pessoas(atividades):
    for i in atividades:
        nova_pessoa = Pessoa(
            nome=i.pessoa,
            descricao=None,
            usuario=i.usuario,
            areas=1
        )

        try:
            pessoa_db = pessoa_service.listar_pessoa_nome(nova_pessoa.nome, nova_pessoa.usuario)
            print('ja tem')
        except ObjectDoesNotExist:
            pessoa_db = pessoa_service.cadastrar_pessoa(nova_pessoa)
            print('cadastrando')

        nova_atividade = Atividade(
            data=i.data,
            area=i.area,
            sub_area=i.sub_area,
            plataforma=i.plataforma,
            pessoa=pessoa_db.id,
            descricao=i.descricao,
            detalhamento=i.detalhamento,
            tempo=i.tempo,
            inicio=i.inicio,
            fim=i.fim,
            usuario=i.usuario
        )
        atividade_service.editar_atividade(i, nova_atividade)