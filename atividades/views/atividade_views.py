from django.shortcuts import render, redirect
from ..services import atividade_service
from ..forms.atividade_form import AtividadeForm
from ..forms.general_form import ExclusaoForm
from ..entidades.atividade import Atividade
from ..repositorios import atividade_repositorio
from datetime import date, datetime
import json
from ..encoder import Encoder
from django.contrib.auth.decorators import login_required

# Create your views here.


template_tags = {'semana_atual': date.today().isocalendar()[1],
                 'mes_atual': date.today().month,
                 'ano_atual': date.today().year,
                 'semana': date.today().isocalendar()[1],
                 'mes': date.today().month,
                 'ano': date.today().year,
                 'tipo': 'semana',
                 'valor': 1,
                 'atividades': None,
                 'tempo_areas': 0,
                 'json_tempo_areas': None,
                 'contador_atividades': 0}


@login_required
def cadastrar_atividade(request):
    if request.method == "POST":
        form_atividade = AtividadeForm(request.POST)
        if form_atividade.is_valid():
            atividade_nova = Atividade(data=form_atividade.cleaned_data['data'],
                                       area=form_atividade.cleaned_data['area'],
                                       sub_area=form_atividade.cleaned_data['sub_area'],
                                       plataforma=form_atividade.cleaned_data['plataforma'],
                                       pessoa=form_atividade.cleaned_data['pessoa'],
                                       descricao=form_atividade.cleaned_data['descricao'],
                                       detalhamento=form_atividade.cleaned_data['detalhamento'],
                                       tempo=form_atividade.cleaned_data['tempo'],
                                       inicio=atividade_service.buscar_inicio().inicio,
                                       fim=datetime.now(),
                                       usuario=request.user)

            atividade_service.cadastrar_atividade(atividade_nova)
            return redirect('listar_semana_atual')
    else:
        form_atividade = AtividadeForm()
        atividade_service.cadastar_inicio()
    template_tags['form_atividade'] = form_atividade
    return render(request, 'atividades/form_atividade.html', template_tags)


@login_required
def listar_atividades(request):
    atividades = atividade_service.listar_atividades(request.user)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    template_tags['contador_atividades'] = len(atividades)
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def listar_ano(request, ano):
    atividades = atividade_service.listar_ano(request.user, ano)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['ano'] = ano
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    template_tags['contador_atividades'] = len(atividades)
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def listar_semana_atual(request):
    atividades = atividade_service.listar_semana_atual(request.user)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    template_tags['contador_atividades'] = len(atividades)
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def listar_ano_mes_semana(request, ano, tipo, valor):
    if tipo == 'mes':
        atividades = atividade_service.listar_mes(request.user, ano, valor)
    elif tipo == 'semana':
        atividades = atividade_service.listar_semana(request.user, ano, valor)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['ano'] = ano
    template_tags['tipo'] = tipo
    template_tags['valor'] = valor
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    template_tags['contador_atividades'] = len(atividades)
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def listar_sessao(request, sessao, valor_sessao):
    if sessao == 'data':
        atividades = atividade_service.listar_data(request.user, valor_sessao)
    elif sessao == 'area':
        atividades = atividade_service.listar_area(request.user, valor_sessao)
    elif sessao == 'sub-area':
        atividades = atividade_service.listar_sub_area(request.user, valor_sessao)
    elif sessao == 'plataforma':
        atividades = atividade_service.listar_plataforma(request.user, valor_sessao)
    elif sessao == 'pessoa':
        atividades = atividade_service.listar_pessoa(request.user, valor_sessao)
    elif sessao == 'descricao':
        atividades = atividade_service.listar_descricao(request.user, valor_sessao)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    template_tags['contador_atividades'] = len(atividades)
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def expandir_atividade(request, id):
    atividade = atividade_service.listar_atividade_id(request.user, id)
    atividades = atividade_service.listar_descricao(request.user, atividade.descricao)
    tempo_total = 0
    tempo_atividade = atividade_repositorio.tempo_atividade(atividade.inicio, atividade.fim)
    for i in atividades:
        tempo_total = tempo_total + i.tempo
    template_tags['atividade'] = atividade
    template_tags['atividades'] = atividades
    template_tags['tempo_total'] = tempo_total
    template_tags['tempo_atividade'] = tempo_atividade
    return render(request, 'atividades/expandir_atividade.html', template_tags)


@login_required
def editar_atividade(request, id):
    atividade_antiga = atividade_service.listar_atividade_id(request.user, id)
    form_atividade = AtividadeForm(request.POST or None, instance=atividade_antiga)
    if form_atividade.is_valid():
        atividade_nova = Atividade(data=form_atividade.cleaned_data['data'],
                                   area=form_atividade.cleaned_data['area'],
                                   sub_area=form_atividade.cleaned_data['sub_area'],
                                   plataforma=form_atividade.cleaned_data['plataforma'],
                                   pessoa=form_atividade.cleaned_data['pessoa'],
                                   descricao=form_atividade.cleaned_data['descricao'],
                                   detalhamento=form_atividade.cleaned_data['detalhamento'],
                                   tempo=form_atividade.cleaned_data['tempo'],
                                   inicio=atividade_antiga.inicio,
                                   fim=atividade_antiga.fim,
                                   usuario=request.user)
        atividade_service.editar_atividade(atividade_antiga, atividade_nova)
        return redirect('listar_semana_atual')
    template_tags['atividade_antiga'] = atividade_antiga
    template_tags['form_atividade'] = form_atividade
    return render(request, 'atividades/editar_atividade.html', template_tags)


def remover_atividade(request, id):
    atividade = atividade_service.listar_atividade_id(request.user, id)
    if request.POST.get('confirmacao'):
        atividade_service.remover_atividade(atividade)
        return redirect('listar_semana_atual')
    template_tags['atividade'] = atividade
    template_tags['form_exclusao'] = ExclusaoForm()
    return render(request, 'atividades/confirma_exclusao.html', template_tags)
