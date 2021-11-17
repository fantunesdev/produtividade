from django.shortcuts import render, redirect
from ..services import area_service
from ..forms.area_form import AreaForm
from ..entidades.area import Area
from datetime import date, datetime

def cadastrar_area(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form_area = AreaForm(request.POST)
            if form_area.is_valid():
                nome = form_area.cleaned_data['nome']
                descricao = form_area.cleaned_data['descricao']

                area_nova = Area(nome=nome, descricao=descricao)
                area_service.cadastrar_area(area_nova)
                return redirect('listar_areas')
        else:
            form_area = AreaForm()
        return render(request, 'atividades/areas/form_area.html', {'form_area': form_area})
    else:
        return redirect(logar_usuario)

def listar_areas(request):
    if request.user.is_authenticated:
        areas = area_service.listar_areas()
        semana_atual = date.today().isocalendar()[1]
        return render(request, 'atividades/areas/listar_areas.html', {'areas': areas,
                                                                      'semana_atual': semana_atual})
    else:
        return redirect(logar_usuario)

def listar_area_id(request, id):
    if request.user.is_authenticated:
        area = area_service.listar_area_id(id)
        semana_atual = date.today().isocalendar()[1]
        return render(request, 'atividades/areas/expandir_area.html', {'area': area,
                                                                      'semana_atual': semana_atual})
    else:
        return redirect(logar_usuario)

def listar_area(request, nome):
    if request.user.is_authenticated:
        area = area_service.listar_area(nome)
        semana_atual = date.today().isocalendar()[1]
        return render(request, 'atividades/areas/expandir_area.html', {'area': area,
                                                                      'semana_atual': semana_atual})
    else:
        return redirect(logar_usuario)

def editar_area(request, id):
    if request.user.is_authenticated:
        area_antiga = area_service.listar_area_id(id)
        form_area = AreaForm(request.POST or None, instance=area_antiga)
        if form_area.is_valid():
            nome = form_area.cleaned_data['nome']
            descricao = form_area.cleaned_data['descricao']

            area_nova = Area(nome=nome, descricao=descricao)

            area_service.editar_area(area_antiga, area_nova)
            return redirect('listar_areas')
        return render(request, 'atividades/areas/form_area.html', {'form_area': form_area, 'area_antiga': area_antiga})

    else:
        return redirect(logar_usuario)

def remover_area(request, id):
    if request.user.is_authenticated:
        area = area_service.listar_area_id(id)
        if request.method == "POST":
            area_service.remover_area(area)
            return redirect('listar_areas')
        return render(request, 'atividades/areas/confirma_exclusao.html', {'area': area})
    else:
        return redirect(logar_usuario)