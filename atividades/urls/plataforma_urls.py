from django.urls import path
from atividades.views.plataforma_view import *

urlpatterns = [
    path('cadastrar/', cadastrar_plataforma, name='cadastrar_plataforma'),
    path('listar/', listar_plataformas, name='listar_plataformas'),
    path('listar/<int:id>/', listar_plataforma_id, name='listar_plataforma_id'),
    path('listar/<str:nome>/', listar_plataforma_nome, name='listar_plataforma_nome'),
    path('editar/<int:id>/', editar_plataforma, name='editar_plataforma'),
    path('remover/<int:id>/', remover_plataforma, name='remover_plataforma')
]