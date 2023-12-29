from django.shortcuts import redirect, render

from atividades.entidades.pessoa import Pessoa
from atividades.forms.general_form import ExclusaoForm
from atividades.forms.pessoa_form import PessoaForm
from atividades.services import pessoa_service
from atividades.views.atividade_views import template_tags


def cadastrar_pessoa(request):
    if request.method == 'POST':
        form_pessoa = PessoaForm(request.POST)
        if form_pessoa.is_valid():
            nova_pessoa = Pessoa(
                nome=form_pessoa.cleaned_data['nome'],
                descricao=form_pessoa.cleaned_data['descricao'],
                usuario=request.user,
                areas=[form_pessoa.cleaned_data['areas']]
            )
            pessoa_service.cadastrar_pessoa(nova_pessoa)
            return redirect('settings')
    else:
        form_pessoa = PessoaForm()
    template_tags['form_pessoa'] = form_pessoa
    return render(request, 'pessoas/form_pessoa.html', template_tags)


def listar_pessoas(request):
    template_tags['pessoas'] = pessoa_service.listar_pessoas(request.user)
    chaves_a_remover = ['areas', 'subareas', 'plataforma']
    for chave in chaves_a_remover:
        if chave in template_tags:
            del template_tags[chave]
    return render(request, 'settings.html', template_tags)


def editar_pessoa(request, id):
    pessoa_antiga = pessoa_service.listar_pessoa_id(id, request.user)
    form_pessoa = PessoaForm(request.POST or None, instance=pessoa_antiga)
    if form_pessoa.is_valid():
        pessoa_nova = Pessoa(
            nome=form_pessoa.cleaned_data['nome'],
            descricao=form_pessoa.cleaned_data['descricao'],
            usuario=request.user,
            areas=[form_pessoa.cleaned_data['areas']]
        )
        pessoa_service.editar_pessoa(pessoa_antiga, pessoa_nova)
        return redirect('settings')
    template_tags['form_pessoa'] = form_pessoa
    template_tags['pessoa_antiga'] = pessoa_antiga
    return render(request, 'pessoas/form_pessoa.html', template_tags)


def remover_pessoa(request, id):
    pessoa = pessoa_service.listar_pessoa_id(id, request.user)
    if request.POST.get('confirmacao'):
        pessoa_service.remover_pessoa(pessoa)
        return redirect('settings')
    template_tags['pessoa'] = pessoa
    template_tags['form_exclusao'] = ExclusaoForm()
    return render(request, 'pessoas/detalhar_pessoa.html', template_tags)
