from ..models import Atividade, InicioAtividade
from datetime import date
from django.utils import timezone


def cadastrar_atividade(atividade):
    nova_atividade = Atividade.objects.create(
        data=atividade.data,
        area=atividade.area,
        sub_area=atividade.sub_area,
        plataforma=atividade.plataforma,
        pessoa=atividade.pessoa,
        descricao=atividade.descricao,
        detalhamento=atividade.detalhamento,
        tempo=atividade.tempo,
        inicio=atividade.inicio,
        fim=atividade.fim,
        usuario=atividade.usuario
    )
    return nova_atividade


def cadastar_inicio():
    agora = timezone.now()
    inicio = validar_primeiro_cadastro_data(agora)
    inicio.inicio = agora
    inicio.save(force_update=True)


def validar_primeiro_cadastro_data(agora):
    data = buscar_inicio()
    if not data:
        InicioAtividade.objects.create(inicio=agora)
        data = buscar_inicio()
    return data


def buscar_inicio():
    inicio = InicioAtividade.objects.filter(id=1).first()
    return inicio


def listar_atividades(usuario):
    atividades = Atividade.objects.filter(usuario=usuario)
    return atividades


def listar_ano(usuario, ano):
    atividades = Atividade.objects.filter(usuario=usuario, data__year=ano)
    return atividades


def listar_mes(usuario, ano, mes):
    atividades = Atividade.objects.filter(usuario=usuario, data__month=mes, data__year=ano)
    return atividades


def listar_semana_atual(usuario):
    semana = date.today().isocalendar()[1]
    ano = date.today().year
    atividades = Atividade.objects.filter(usuario=usuario, data__week=semana, data__year=ano)
    return atividades


def listar_semana(usuario, ano, semana):
    atividades = Atividade.objects.filter(usuario=usuario, data__week=semana, data__year=ano)
    return atividades


def listar_data(usuario, data):
    atividades = Atividade.objects.filter(usuario=usuario, data=data)
    return atividades


def listar_area(usuario, area):
    atividades = Atividade.objects.filter(usuario=usuario, area__nome=area)
    return atividades


def listar_sub_area(usuario, sub_area):
    atividades = Atividade.objects.filter(usuario=usuario, sub_area=sub_area.replace("-", " "))
    return atividades


def listar_plataforma(usuario, plataforma):
    atividades = Atividade.objects.filter(usuario=usuario, plataforma=plataforma.replace("-", " "))
    return atividades


def listar_pessoa(usuario, pessoa):
    atividades = Atividade.objects.filter(usuario=usuario, pessoa=pessoa)
    return atividades


def listar_descricao(usuario, descricao):
    atividades = Atividade.objects.filter(usuario=usuario, descricao=descricao)
    return atividades


def listar_detalhamento(usuario, detalhamento):
    atividades = Atividade.objects.filter(usuario=usuario, detalhamento__contains=detalhamento)
    return atividades


def listar_atividade_id(usuario, id):
    atividade = Atividade.objects.get(usuario=usuario, id=id)
    return atividade


def editar_atividade(atividade, atividade_nova):
    atividade.data = atividade_nova.data
    atividade.area = atividade_nova.area
    atividade.sub_area = atividade_nova.sub_area
    atividade.plataforma = atividade_nova.plataforma
    atividade.pessoa = atividade_nova.pessoa
    atividade.descricao = atividade_nova.descricao
    atividade.detalhamento = atividade_nova.detalhamento
    atividade.tempo = atividade_nova.tempo
    atividade.save(force_update=True)
    return atividade


def remover_atividade(atividade):
    atividade.delete()
