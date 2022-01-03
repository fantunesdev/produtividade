from django.shortcuts import render, redirect
from ..services import area_service
from ..forms.area_form import AreaForm
from ..entidades.area import Area
from ..views.usuario_view import logar_usuario
from ..views.atividade_views import template_tags


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
        template_tags['form_area'] = form_area
        return render(request, 'atividades/areas/form_area.html', template_tags)
    else:
        return redirect(logar_usuario)


def listar_areas(request):
    if request.user.is_authenticated:
        areas = area_service.listar_areas()
        template_tags['areas'] = areas
        return render(request, 'atividades/areas/listar_areas.html', template_tags)
    else:
        return redirect(logar_usuario)


def listar_area_id(request, id):
    if request.user.is_authenticated:
        area = area_service.listar_area_id(id)
        template_tags['area'] = area
        return render(request, 'atividades/areas/expandir_area.html', template_tags)
    else:
        return redirect(logar_usuario)


def listar_area(request, nome):
    if request.user.is_authenticated:
        area = area_service.listar_area(nome)
        template_tags['area'] = area
        return render(request, 'atividades/areas/expandir_area.html', template_tags)
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
        template_tags['form_area'] = form_area
        template_tags['area_antiga'] = area_antiga
        return render(request, 'atividades/areas/form_area.html', template_tags)

    else:
        return redirect(logar_usuario)


def remover_area(request, id):
    if request.user.is_authenticated:
        area = area_service.listar_area_id(id)
        if request.method == "POST":
            area_service.remover_area(area)
            return redirect('listar_areas')
        template_tags['area'] = area
        return render(request, 'atividades/areas/confirma_exclusao.html', template_tags)
    else:
        return redirect(logar_usuario)