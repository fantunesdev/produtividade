from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from atividades.entidades.plataforma import Plataforma
from atividades.forms.general_form import ExclusaoForm
from atividades.forms.plataforma_form import PlataformaForm
from atividades.services import plataforma_service
from atividades.views.atividade_views import template_tags


@login_required
def cadastrar_plataforma(request):
    if request.method == "POST":
        form_plataforma = PlataformaForm(request.POST)
        if form_plataforma.is_valid():
            plataforma_nova = Plataforma(
                nome=form_plataforma.cleaned_data['nome'],
                descricao=form_plataforma.cleaned_data['descricao'],
                usuario=request.user,
                areas=form_plataforma.cleaned_data['areas']
            )
            plataforma_service.cadastrar_plataforma(plataforma_nova)
            return redirect('settings')
    else:
        form_plataforma = PlataformaForm()
    template_tags['form_plataforma'] = form_plataforma
    return render(request, 'plataformas/form_plataforma.html', template_tags)


def listar_plataformas(request):
    plataformas = plataforma_service.listar_plataformas(request.user)
    template_tags['plataformas'] = plataformas
    chaves_a_remover = ['areas', 'subareas', 'pessoas']
    for chave in chaves_a_remover:
        if chave in template_tags:
            del template_tags[chave]
    return render(request, 'settings.html', template_tags)


@login_required()
def editar_plataforma(request, id):
    plataforma_antiga = plataforma_service.listar_plataforma_id(id, request.user)
    form_plataforma = PlataformaForm(request.POST or None, instance=plataforma_antiga)
    if form_plataforma.is_valid():
        plataforma_nova = Plataforma(
            nome=form_plataforma.cleaned_data['nome'],
            descricao=form_plataforma.cleaned_data['descricao'],
            usuario=request.user,
            areas=[form_plataforma.cleaned_data['areas']],
        )
        plataforma_service.editar_plataforma(plataforma_antiga, plataforma_nova)
        return redirect('settings')
    template_tags['form_plataforma'] = form_plataforma
    template_tags['plataforma_antiga'] = plataforma_antiga
    return render(request, 'plataformas/form_plataforma.html', template_tags)


@login_required()
def remover_plataforma(request, id):
    plataforma = plataforma_service.listar_plataforma_id(id, request.user)
    if request.POST.get('confirmacao'):
        plataforma_service.remover_plataforma(plataforma)
        return redirect('settings')
    template_tags['plataforma'] = plataforma
    template_tags['form_exclusao'] = ExclusaoForm()
    return render(request, 'plataformas/detalhar_plataforma.html', template_tags)
