from django.urls import path
from atividades.views.atividade_views import *

urlpatterns = [
    path('', listar_semana_atual, name='listar_semana_atual'),
    path('cadastrar/', cadastrar_atividade, name='cadastrar_atividade'),
    path('editar/<int:id>/', editar_atividade, name='editar_atividade'),
    path('listar/', listar_atividades, name='listar_atividades'),
    path('listar/ano_<int:ano>/<str:tipo>_<int:valor>/', listar_ano_mes_semana, name='listar_ano_mes_semana'),
    path('listar/ano_<int:ano>/', listar_ano, name='listar_ano'),
    path('listar/<int:id>', expandir_atividade, name='expandir_atividade'),
    path('listar/<str:sessao>/<str:valor_sessao>/', listar_sessao, name='listar_sessao'),
    path('remover/<int:id>', remover_atividade, name='remover_atividade'),
    path('settings/', settings, name='settings'),
    path('buscar/', buscar, name='buscar')
]

