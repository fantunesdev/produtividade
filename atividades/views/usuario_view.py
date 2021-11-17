from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from datetime import date, datetime

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_semana_atual')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'atividades/usuarios/cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    semana_atual = date.today().isocalendar()[1]
    if request.method == "POST":
        form_usuario = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_semana_atual')
        else:
            form_usuario = AuthenticationForm()
    else:
        form_usuario = AuthenticationForm()
    return render(request, 'atividades/usuarios/login.html', {'form_usuario': form_usuario,
                                                              'semana_atual': semana_atual})

def deslogar_usuario(request):
    logout(request)
    return redirect('listar_semana_atual')
