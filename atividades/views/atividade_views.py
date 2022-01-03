from django.shortcuts import render, redirect
from ..services import atividade_service
from ..forms.atividade_form import AtividadeForm, AtividadeFormVer, ExclusaoForm
from ..entidades.atividade import Atividade
from ..repositorios import atividade_repositorio
from datetime import date, datetime
from ..views.usuario_view import logar_usuario
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


def cadastrar_atividade(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form_atividade = AtividadeForm(request.POST)
            if form_atividade.is_valid():
                data = form_atividade.cleaned_data['data']
                area = form_atividade.cleaned_data['area']
                sub_area = form_atividade.cleaned_data['sub_area']
                plataforma = form_atividade.cleaned_data['plataforma']
                pessoa = form_atividade.cleaned_data['pessoa']
                descricao = form_atividade.cleaned_data['descricao']
                detalhamento = form_atividade.cleaned_data['detalhamento']
                tempo = form_atividade.cleaned_data['tempo']
                inicio = atividade_service.buscar_inicio()[0].inicio
                fim = datetime.now()
                usuario = request.user

                atividade_nova = Atividade(data=data, area=area,
                                           sub_area=sub_area,
                                           plataforma=plataforma,
                                           pessoa=pessoa,
                                           descricao=descricao,
                                           detalhamento=detalhamento,
                                           tempo=tempo,
                                           inicio=inicio,
                                           fim=fim,
                                           usuario=usuario)

                atividade_service.cadastrar_atividade(atividade_nova)
                return redirect('listar_semana_atual')
        else:
            form_atividade = AtividadeForm()
            atividade_service.cadastar_inicio()
        template_tags['form_atividade'] = form_atividade
        return render(request, 'atividades/atividades/form_atividade.html', template_tags)
    else:
        return redirect(logar_usuario)

def listar_atividades(request):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_atividades(request.user)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

def listar_ano(request, ano):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_ano(request.user, ano)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

def listar_semana_atual(request):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_semana_atual(request.user)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

@login_required
def listar_tipo(request, ano, tipo, valor):
    if request.user.is_authenticated:
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

        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

def listar_por_data(request, data):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_data(request.user, data)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

def listar_por_area(request, area):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_area(request.user, area)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)

def listar_por_sub_area(request, sub_area):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_sub_area(request.user, sub_area)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

def listar_por_plataforma(request, plataforma):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_plataforma(request.user, plataforma)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

def listar_por_pessoa(request, pessoa):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_pessoa(request.user, pessoa)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

def listar_por_descricao(request, descricao):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_descricao(request.user, descricao)
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        template_tags['atividades'] = atividades
        template_tags['tempo_areas'] = tempo_areas
        template_tags['json_tempo_areas'] = json_tempo_areas
        template_tags['contador_atividades'] = len(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', template_tags)
    else:
        return redirect(logar_usuario)

def expandir_atividade(request, id):
    if request.user.is_authenticated:
        atividade = atividade_service.listar_atividade_id(request.user, id)
        atividades = atividade_service.listar_por_descricao(request.user, atividade.descricao)
        tempo_total = 0
        for i in atividades:
            tempo_total = tempo_total + i.tempo
        template_tags['atividade'] = atividade
        template_tags['tempo_total'] = tempo_total
        return render(request, 'atividades/atividades/expandir_atividade.html', template_tags)
    else:
        return redirect(logar_usuario)

def editar_atividade(request, id):
    if request.user.is_authenticated:
        atividade_antiga = atividade_service.listar_atividade_id(request.user, id)
        form_atividade = AtividadeForm(request.POST or None, instance=atividade_antiga)
        if form_atividade.is_valid():
            data = form_atividade.cleaned_data['data']
            area = form_atividade.cleaned_data['area']
            sub_area = form_atividade.cleaned_data['sub_area']
            plataforma = form_atividade.cleaned_data['plataforma']
            pessoa = form_atividade.cleaned_data['pessoa']
            descricao = form_atividade.cleaned_data['descricao']
            detalhamento = form_atividade.cleaned_data['detalhamento']
            tempo = form_atividade.cleaned_data['tempo']
            inicio = atividade_antiga.inicio
            fim = atividade_antiga.fim
            usuario = request.user

            atividade_nova = Atividade(data=data, area=area,
                                       sub_area=sub_area,
                                       plataforma=plataforma,
                                       pessoa=pessoa,
                                       descricao=descricao,
                                       detalhamento=detalhamento,
                                       tempo=tempo,
                                       inicio=inicio,
                                       fim=fim,
                                       usuario=usuario)
            atividade_service.editar_atividade(atividade_antiga, atividade_nova)
            return redirect('listar_semana_atual')
        template_tags['atividade_antiga'] = atividade_antiga
        template_tags['form_atividade'] = form_atividade
        return render(request, 'atividades/atividades/editar_atividade.html', template_tags)
    else:
        return redirect(logar_usuario)

def remover_atividade(request, id):
    if request.user.is_authenticated:
        atividade = atividade_service.listar_atividade_id(request.user, id)
        if request.method == "POST":
            form_exclusao = ExclusaoForm(request.POST)
            if form_exclusao.is_valid():
                confirmacao = form_exclusao.cleaned_data['confirmacao']
                if confirmacao == True:
                    atividade_service.remover_atividade(atividade)
                    return redirect('listar_semana_atual')
        else:
            form_exclusao = ExclusaoForm()
        template_tags['atividade'] = atividade
        template_tags['form_exclusao'] = form_exclusao
        return render(request, 'atividades/atividades/confirma_exclusao.html', template_tags)
    else:
        return redirect(logar_usuario)
