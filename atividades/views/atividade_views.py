from django.shortcuts import render, redirect
from ..services import atividade_service
from ..forms.atividade_form import AtividadeForm, AtividadeFormVer, ExclusaoForm
from ..entidades.atividade import Atividade
from ..repositorios import atividade_repositorio
from datetime import date, datetime
from ..views.usuario_view import logar_usuario
import json
from ..encoder import Encoder

# Create your views here.

def cadastrar_atividade(request):
    if request.user.is_authenticated:
        semana_atual = date.today().isocalendar()[1]
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
        return render(request, 'atividades/atividades/form_atividade.html', {'form_atividade': form_atividade,
                                                                             'semana_atual': semana_atual})
    else:
        return redirect(logar_usuario)

def listar_atividades(request):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_atividades(request.user)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_por_ano(request):
    if request.user.is_authenticated:
        ano = 2021
        atividades = atividade_service.listar_por_ano(request.user, ano)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_por_mes(request, mes):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_mes(request.user, mes)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_semana_atual(request):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_semana_atual(request.user)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_por_semana(request, semana):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_semana(request.user, semana)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_por_data(request, data):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_data(request.user, data)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_por_area(request, area):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_area(request.user, area)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})

def listar_por_sub_area(request, sub_area):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_sub_area(request.user, sub_area)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_por_plataforma(request, plataforma):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_plataforma(request.user, plataforma)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_por_pessoa(request, pessoa):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_pessoa(request.user, pessoa)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def listar_por_descricao(request, descricao):
    if request.user.is_authenticated:
        atividades = atividade_service.listar_por_descricao(request.user, descricao)
        semana_atual = date.today().isocalendar()[1]
        tempo_areas = atividade_repositorio.calcular_tempo_atividade_area(atividades)
        json_tempo_areas = json.dumps(tempo_areas, cls=Encoder)
        contador_atividades = atividade_repositorio.contador_atividades(atividades)
        return render(request, 'atividades/atividades/listar_atividades.html', {'semana_atual': semana_atual,
                                                                                'atividades': atividades,
                                                                                'tempo_areas': tempo_areas,
                                                                                'contador_atividades': contador_atividades,
                                                                                'json_tempo_areas': json_tempo_areas})
    else:
        return redirect(logar_usuario)

def expandir_atividade(request, id):
    if request.user.is_authenticated:
        semana_atual = date.today().isocalendar()[1]
        atividade = atividade_service.listar_atividade_id(request.user, id)
        atividades = atividade_service.listar_por_descricao(request.user, atividade.descricao)
        tempo_atividade = atividade_repositorio.tempo_atividade(atividade.inicio, atividade.fim)
        tempo_total = 0
        for i in atividades:
            tempo_total = tempo_total + i.tempo
        return render(request, 'atividades/atividades/expandir_atividade.html', {'atividade': atividade,
                                                                                 'atividades': atividades,
                                                                                 'tempo_atividade': tempo_atividade,
                                                                                 'tempo_total': tempo_total,
                                                                                 'semana_atual': semana_atual})
    else:
        return redirect(logar_usuario)

def editar_atividade(request, id):
    if request.user.is_authenticated:
        semana_atual = date.today().isocalendar()[1]
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
        return render(request, 'atividades/atividades/editar_atividade.html', {'form_atividade': form_atividade,
                                                                               'atividade_antiga': atividade_antiga,
                                                                               'semana_atual': semana_atual})
    else:
        return redirect(logar_usuario)

def remover_atividade(request, id):
    if request.user.is_authenticated:
        semana_atual = date.today().isocalendar()[1]
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
        return render(request, 'atividades/atividades/confirma_exclusao.html', {'atividade': atividade,
                                                                                'semana_atual': semana_atual,
                                                                                'form_exclusao': form_exclusao})
    else:
        return redirect(logar_usuario)
