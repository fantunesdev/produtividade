from ..models import Atividade, InicioAtividade
from datetime import date
from django.utils import timezone


def cadastrar_atividade(atividade):
    try:
        nova_atividade = Atividade.objects.create(
            data=atividade.data,
            area=atividade.area,
            subarea=atividade.subarea,
            plataforma=atividade.plataforma,
            pessoa=atividade.pessoa,
            descricao=atividade.descricao,
            detalhamento=atividade.detalhamento,
            tempo=atividade.tempo,
            inicio=atividade.inicio,
            fim=atividade.fim,
            usuario=atividade.usuario
        )
        print('cadastrou')
        return nova_atividade
    except:
        print('nao cadastrou')


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
    return InicioAtividade.objects.filter(id=1).first()


def listar_atividades(usuario):
    return Atividade.objects.filter(usuario=usuario)


def listar_ano(usuario, ano):
    return Atividade.objects.filter(usuario=usuario, data__year=ano)


def listar_mes(usuario, ano, mes):
    return Atividade.objects.filter(usuario=usuario, data__month=mes, data__year=ano)


def listar_semana_atual(usuario):
    semana = date.today().isocalendar()[1]
    ano = date.today().year
    return Atividade.objects.filter(usuario=usuario, data__week=semana, data__year=ano)


def listar_semana(usuario, ano, semana):
    return Atividade.objects.filter(usuario=usuario, data__week=semana, data__year=ano)


def listar_data(usuario, data):
    return Atividade.objects.filter(usuario=usuario, data=data)


def listar_area(usuario, area):
    return Atividade.objects.filter(usuario=usuario, area=area)


def listar_subarea(usuario, subarea):
    return Atividade.objects.filter(usuario=usuario, subarea=subarea)


def listar_plataforma(usuario, plataforma):
    return Atividade.objects.filter(usuario=usuario, plataforma=plataforma)


def listar_pessoa(usuario, pessoa):
    return Atividade.objects.filter(usuario=usuario, pessoa=pessoa)


def listar_descricao(usuario, descricao):
    return Atividade.objects.filter(usuario=usuario, descricao=descricao)


def listar_detalhamento(usuario, detalhamento):
    return Atividade.objects.filter(usuario=usuario, detalhamento__contains=detalhamento)


def listar_atividade_id(usuario, id):
    return Atividade.objects.get(usuario=usuario, id=id)


def editar_atividade(atividade, atividade_nova):
    atividade.data = atividade_nova.data
    atividade.area = atividade_nova.area
    atividade.subarea = atividade_nova.subarea
    atividade.plataforma = atividade_nova.plataforma
    atividade.pessoa = atividade_nova.pessoa
    atividade.descricao = atividade_nova.descricao
    atividade.detalhamento = atividade_nova.detalhamento
    atividade.tempo = atividade_nova.tempo
    atividade.save(force_update=True)
    return atividade


def remover_atividade(atividade):
    atividade.delete()
