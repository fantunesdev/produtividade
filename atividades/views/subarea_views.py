from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from atividades.entidades.subarea import SubArea
from atividades.forms.general_form import ExclusaoForm
from atividades.forms.subarea_form import SubAreaForm
from atividades.services import subarea_service
from atividades.views.atividade_views import template_tags


@login_required
def cadastrar_subarea(request):
    if request.method == 'POST':
        form_subarea = SubAreaForm(request.POST)
        if form_subarea.is_valid():
            nova_subarea = SubArea(
                nome=form_subarea.cleaned_data['nome'],
                descricao=form_subarea.cleaned_data['descricao'],
                usuario=request.user,
                areas=form_subarea.cleaned_data['areas']
            )
            subarea_service.cadastrar_subarea(nova_subarea)
            return redirect('settings')
    else:
        form_subarea = SubAreaForm()
    template_tags['form_subarea'] = form_subarea
    template_tags['subarea_antiga'] = None
    return render(request, 'subareas/form_subarea.html', template_tags)


@login_required
def listar_subareas(request):
    subareas = subarea_service.listar_subareas(request.user)
    chaves_a_remover = ['areas', 'plataforma', 'pessoas']
    for chave in chaves_a_remover:
        if chave in template_tags:
            del template_tags[chave]
    template_tags['subareas'] = subareas
    print(template_tags['subareas'])
    return render(request, 'settings.html', template_tags)


@login_required
def listar_subarea_id(request, id):
    subarea = subarea_service.listar_subarea_id(request.user, id)
    template_tags['subarea'] = subarea
    return render(request, 'subareas/detalhar_subarea.html', template_tags)


@login_required
def listar_subarea_nome(request, nome):
    subarea = subarea_service.listar_subarea_nome(request.user, nome)
    template_tags['subarea'] = subarea
    return render(request, 'subareas/detalhar_subarea.html', template_tags)


@login_required
def editar_subarea(request, id):
    subarea_antiga = subarea_service.listar_subarea_id(request.user, id)
    form_subarea = SubAreaForm(request.POST or None, instance=subarea_antiga)
    if form_subarea.is_valid():
        subarea_nova = SubArea(
            nome=form_subarea.cleaned_data['nome'],
            descricao=form_subarea.cleaned_data['descricao'],
            areas=[form_subarea.cleaned_data['areas']],
            usuario=request.user
        )
        subarea_service.editar_subarea(subarea_antiga, subarea_nova)
        return redirect('settings')
    template_tags['form_subarea'] = form_subarea
    template_tags['subarea_antiga'] = subarea_antiga
    return render(request, 'subareas/form_subarea.html', template_tags)


@login_required
def remover_subarea(request, id):
    subarea = subarea_service.listar_subarea_id(request.user, id)
    if request.POST.get('confirmacao'):
        subarea_service.remover_subarea(subarea)
        return redirect('settings')
    template_tags['subarea'] = subarea
    template_tags['form_exclusao'] = ExclusaoForm()
    return render(request, 'subareas/detalhar_subarea.html', template_tags)
