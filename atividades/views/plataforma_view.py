from django.shortcuts import render, redirect
from ..services import plataforma_service
from ..forms.plataforma_form import PlataformaForm
from ..entidades.plataforma import Plataforma

def cadastrar_plataforma(request):
    if request.method == "POST":
        form_plataforma = PlataformaForm(request.POST)
        if form_plataforma.is_valid():
            nome = form_plataforma.cleaned_data['nome']
            descricao = form_plataforma.cleaned_data['descricao']
            plataforma_nova = Plataforma(nome=nome, descricao=descricao)
            plataforma_service.cadastrar_plataforma(plataforma_nova)
            return redirect('listar_plataformas')
    else:
        form_plataforma = PlataformaForm()
    return render(request, 'plataformas/form_plataforma.html', {'form_plataforma': form_plataforma})

def listar_plataformas(request):
    plataformas = plataforma_service.listar_plataformas()
    print(plataformas)
    return render(request, 'plataformas/listar_plataforma.html', {'plataformas': plataformas} )

def listar_plataforma_id(request, id):
    plataforma = plataforma_service.listar_plataformas(id)
    return render(request, 'plataformas/expandir_plataforma.html', {'plataforma': plataforma})

def listar_plataforma_nome(request, nome):
    plataforma = plataforma_service.listar_plataforma_nome(nome)
    return render(request, 'plataformas/expandir_plataforma.html', {'plataforma': plataforma})

def editar_plataforma(request, id):
    pass

def remover_plataforma(request, id):
    pass