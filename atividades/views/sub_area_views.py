from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..entidades.sub_area import SubArea
from ..services import sub_area_service
from ..views.atividade_views import template_tags
from atividades.forms.sub_area_form import SubAreaForm
from atividades.forms.general_form import ExclusaoForm


@login_required
def cadastrar_sub_area(request):
    if request.method == 'POST':
        form_sub_area = SubAreaForm(request.POST)
        if form_sub_area.is_valid():
            nova_sub_area = SubArea(nome=form_sub_area.cleaned_data['nome'],
                                    descricao=form_sub_area.cleaned_data['descricao'],
                                    area=form_sub_area.cleaned_data['area'],
                                    usuario=request.user)
            sub_area_service.cadastrar_sub_area(nova_sub_area)
            return redirect('listar_sub_areas')
    else:
        form_sub_area = SubAreaForm()
    template_tags['form_sub_area'] = form_sub_area
    return render(request, 'atividades/sub_areas/form_sub_area.html', template_tags)


@login_required
def listar_sub_areas(request):
    sub_areas = sub_area_service.listar_sub_areas(request.user)
    template_tags['sub_areas'] = sub_areas
    return render(request, 'atividades/sub_areas/listar_sub_areas.html', template_tags)


@login_required
def listar_sub_area_id(request, id):
    sub_area = sub_area_service.listar_sub_area_id(request.user, id)
    template_tags['sub_area'] = sub_area
    print(sub_area.nome)
    return render(request, 'atividades/sub_areas/expandir_sub_area.html', template_tags)


@login_required
def listar_sub_area_nome(request, nome):
    sub_area = sub_area_service.listar_sub_area_nome(request.user, nome)
    template_tags['sub_area'] = sub_area
    return render(request, 'atividades/sub_areas/expandir_sub_area.html', template_tags)



@login_required
def editar_sub_area(request, id):
    sub_area_antiga = sub_area_service.listar_sub_area_id(request.user, id)
    form_sub_area = SubAreaForm(request.POST or None, instance=sub_area_antiga)
    if form_sub_area.is_valid():
        sub_area_nova = SubArea(nome=form_sub_area.cleaned_data['nome'],
                                descricao=form_sub_area.cleaned_data['descricao'],
                                area=form_sub_area.cleaned_data['area'],
                                usuario=request.user)
        sub_area_service.editar_sub_area(sub_area_antiga, sub_area_nova)
        return redirect('listar_sub_areas')
    template_tags['form_sub_area'] = form_sub_area
    template_tags['sub_area_antiga'] = sub_area_antiga
    return render(request, 'atividades/sub_areas/editar_sub_area.html', template_tags)


@login_required
def remover_sub_area(request, id):
    sub_area = sub_area_service.listar_sub_area_id(request.user, id)
    if request.method == 'POST':
        form_exclusao = ExclusaoForm()
        print(request.POST.get('confirmacao'))
        if request.POST.get('confirmacao'):
            sub_area_service.remover_sub_area(sub_area)
            return redirect('listar_sub_areas')
    else:
        form_exclusao = ExclusaoForm()
    template_tags['sub_area'] = sub_area
    template_tags['form_exclusao'] = form_exclusao
    return render(request, 'atividades/sub_areas/confirma_exclusao.html', template_tags)
