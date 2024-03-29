from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from atividades.entidades.area import Area
from atividades.forms.area_form import AreaForm
from atividades.forms.general_form import ExclusaoForm
from atividades.services import area_service
from atividades.views.atividade_views import template_tags


@login_required
def cadastrar_area(request):
    if request.method == "POST":
        form_area = AreaForm(request.POST)
        if form_area.is_valid():
            area_nova = Area(
                nome=form_area.cleaned_data['nome'],
                descricao=form_area.cleaned_data['descricao'],
                cor=form_area.cleaned_data['cor'],
                usuario=request.user
            )
            area_service.cadastrar_area(area_nova)
            return redirect('settings')
    else:
        form_area = AreaForm()
    template_tags['form_area'] = form_area
    return render(request, 'areas/form_area.html', template_tags)


@login_required
def listar_areas(request):
    areas = area_service.listar_areas(request.user)
    template_tags['areas'] = areas
    chaves_a_remover = ['subareas', 'plataforma', 'pessoas']
    for chave in chaves_a_remover:
        if chave in template_tags:
            del template_tags[chave]
    return render(request, 'settings.html', template_tags)


@login_required
def listar_area(request, nome):
    area = area_service.listar_area(request.user, nome)
    template_tags['area'] = area
    return render(request, 'areas/detalhar_area.html', template_tags)


@login_required
def editar_area(request, id):
    area_antiga = area_service.listar_area_id(id, request.user)
    form_area = AreaForm(request.POST or None, instance=area_antiga)
    if form_area.is_valid():
        area_nova = Area(
            nome=form_area.cleaned_data['nome'],
            descricao=form_area.cleaned_data['descricao'],
            cor=form_area.cleaned_data['cor'],
            usuario=request.user
        )

        area_service.editar_area(area_antiga, area_nova)
        return redirect('settings')
    template_tags['form_area'] = form_area
    template_tags['area_antiga'] = area_antiga
    return render(request, 'areas/form_area.html', template_tags)


@login_required
def remover_area(request, id):
    area = area_service.listar_area_id(id, request.user)
    if request.POST.get('confirmacao'):
        area_service.remover_area(area)
        return redirect('settings')
    template_tags['area'] = area
    template_tags['form_exclusao'] = ExclusaoForm()
    return render(request, 'areas/detalhar_area.html', template_tags)
