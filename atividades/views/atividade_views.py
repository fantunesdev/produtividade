import json

from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from atividades.encoder import Encoder
from atividades.entidades.atividade import Atividade
from atividades.forms.atividade_form import AtividadeForm, AtividadeBuscar, AtividadeEmLoteForm
from atividades.forms.general_form import ExclusaoForm
from atividades.repositorios import atividade_repositorio
from atividades.services import atividade_service, area_service, subarea_service, plataforma_service, pessoa_service

# Create your views here.


template_tags = {
    'semana_atual': date.today().isocalendar()[1],
    'mes_atual': date.today().month,
    'ano_atual': date.today().year,
    'semana': date.today().isocalendar()[1],
    'mes': date.today().month,
    'ano': date.today().year,
    'tipo': 'semana',
    'valor': 1,
    'atividades': None,
    'tempo_areas': 0,
    'json_tempo_areas': None
}


@login_required
def cadastrar_atividade(request):
    if request.method == "POST":
        form_atividade = AtividadeForm(request.POST)
        if form_atividade.is_valid():
            atividade_nova = Atividade(
                data=form_atividade.cleaned_data['data'],
                area=form_atividade.cleaned_data['area'],
                subarea=form_atividade.cleaned_data['subarea'],
                plataforma=form_atividade.cleaned_data['plataforma'],
                pessoa=form_atividade.cleaned_data['pessoa'],
                descricao=form_atividade.cleaned_data['descricao'],
                detalhamento=form_atividade.cleaned_data['detalhamento'],
                tempo=form_atividade.cleaned_data['tempo'],
                inicio=atividade_service.buscar_inicio().inicio,
                fim=timezone.now(),
                usuario=request.user
            )

            atividade_service.cadastrar_atividade(atividade_nova)
            return redirect('listar_semana_atual')
    else:
        form_atividade = AtividadeForm()
        atividade_service.cadastar_inicio()
    template_tags['form_atividade'] = form_atividade
    return render(request, 'atividades/form_atividade.html', template_tags)


@login_required
def cadastrar_atividade_em_lote(request):
    if request.method == "POST":
        form_atividade = AtividadeEmLoteForm(request.POST)
        if form_atividade.is_valid():
            data_inicial = form_atividade.cleaned_data['data']
            data_final = form_atividade.cleaned_data['data_final']
            dias = (data_final - data_inicial).days
            dias_da_semana_selecionados = form_atividade.cleaned_data['dias_da_semana']
            print(dias_da_semana_selecionados)
            for i in range(dias + 1):
                dia = data_inicial + timedelta(days=i)
                print(dia.weekday())
                print(f'{dia.weekday()}' in dias_da_semana_selecionados)
                if f'{dia.weekday()}' in dias_da_semana_selecionados:
                    print('entrou')
                    atividade_nova = Atividade(
                        data=dia,
                        area=form_atividade.cleaned_data['area'],
                        subarea=form_atividade.cleaned_data['subarea'],
                        plataforma=form_atividade.cleaned_data['plataforma'],
                        pessoa=form_atividade.cleaned_data['pessoa'],
                        descricao=form_atividade.cleaned_data['descricao'],
                        detalhamento=form_atividade.cleaned_data['detalhamento'],
                        tempo=form_atividade.cleaned_data['tempo'],
                        inicio=atividade_service.buscar_inicio().inicio,
                        fim=timezone.now(),
                        usuario=request.user
                    )

                    atividade_service.cadastrar_atividade(atividade_nova)
            return redirect('listar_semana_atual')
    else:
        form_atividade = AtividadeEmLoteForm()
        atividade_service.cadastar_inicio()
    template_tags['form_atividade'] = form_atividade
    return render(request, 'atividades/form_atividade.html', template_tags)


@login_required
def listar_atividades(request):
    atividades = atividade_service.listar_atividades(request.user)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades, request.user)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def listar_ano(request, ano):
    atividades = atividade_service.listar_ano(request.user, ano)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades, request.user)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['ano'] = ano
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def listar_semana_atual(request):
    atividades = atividade_service.listar_semana_atual(request.user)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades, request.user)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['valor'] = date.today().isocalendar()[1]
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def listar_ano_mes_semana(request, ano, tipo, valor):
    if tipo == 'mes':
        atividades = atividade_service.listar_mes(request.user, ano, valor)
    elif tipo == 'semana':
        atividades = atividade_service.listar_semana(request.user, ano, valor)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades, request.user)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['ano'] = ano
    template_tags['tipo'] = tipo
    template_tags['valor'] = valor
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def listar_sessao(request, sessao, valor_sessao):
    if sessao == 'data':
        atividades = atividade_service.listar_data(request.user, valor_sessao)
    elif sessao == 'areas':
        atividades = atividade_service.listar_area(request.user, valor_sessao)
    elif sessao == 'subareas':
        atividades = atividade_service.listar_subarea(request.user, valor_sessao)
    elif sessao == 'plataformas':
        atividades = atividade_service.listar_plataforma(request.user, valor_sessao)
    elif sessao == 'pessoas':
        atividades = atividade_service.listar_pessoa(request.user, valor_sessao)
    elif sessao == 'descricao':
        atividades = atividade_service.listar_descricao(request.user, valor_sessao)
    tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades, request.user)
    json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
    template_tags['atividades'] = atividades
    template_tags['tempo_areas'] = tempo_areas
    template_tags['json_tempo_areas'] = json_tempo_areas
    return render(request, 'atividades/listar_atividades.html', template_tags)


@login_required
def buscar(request):
    if request.method == 'POST':
        form_atividade = AtividadeBuscar(request.POST)
        if form_atividade.is_valid():
            detalhamento = form_atividade.cleaned_data['detalhamento']
            atividades = atividade_service.listar_detalhamento(request.user, detalhamento)
            template_tags['atividades'] = atividades
            template_tags['form_atividade'] = form_atividade
            return render(request, 'atividades/detalhar_atividade.html', template_tags)
    else:
        form_atividade = AtividadeBuscar()
        template_tags['form_atividade'] = form_atividade
        return render(request, 'atividades/buscar.html', template_tags)


@login_required
def detalhar_atividade(request, id):
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
    template_tags['projeto'] = True
    return render(request, 'atividades/detalhar_atividade.html', template_tags)


@login_required
def editar_atividade(request, id):
    atividade_antiga = atividade_service.listar_atividade_id(request.user, id)
    form_atividade = AtividadeForm(request.POST or None, instance=atividade_antiga)
    if form_atividade.is_valid():
        atividade_nova = Atividade(
            data=form_atividade.cleaned_data['data'],
            area=form_atividade.cleaned_data['area'],
            subarea=form_atividade.cleaned_data['subarea'],
            plataforma=form_atividade.cleaned_data['plataforma'],
            pessoa=form_atividade.cleaned_data['pessoa'],
            descricao=form_atividade.cleaned_data['descricao'],
            detalhamento=form_atividade.cleaned_data['detalhamento'],
            tempo=form_atividade.cleaned_data['tempo'],
            inicio=atividade_antiga.inicio,
            fim=atividade_antiga.fim,
            usuario=request.user
        )
        atividade_service.editar_atividade(atividade_antiga, atividade_nova)
        return redirect('listar_semana_atual')
    template_tags['atividade_antiga'] = atividade_antiga
    template_tags['form_atividade'] = form_atividade
    return render(request, 'atividades/form_atividade.html', template_tags)


def remover_atividade(request, id):
    atividade = atividade_service.listar_atividade_id(request.user, id)
    if request.POST.get('confirmacao'):
        atividade_service.remover_atividade(atividade)
        return redirect('listar_semana_atual')
    template_tags['atividade'] = atividade
    template_tags['form_exclusao'] = ExclusaoForm()
    template_tags['tempo_total'] = 0
    return render(request, 'atividades/detalhar_atividade.html', template_tags)


def settings(request):
    template_tags['areas'] = area_service.listar_areas(request.user)
    template_tags['subareas'] = subarea_service.listar_subareas(request.user)
    template_tags['plataformas'] = plataforma_service.listar_plataformas(request.user)
    template_tags['pessoas'] = pessoa_service.listar_pessoas(request.user)
    return render(request, 'settings.html', template_tags)
