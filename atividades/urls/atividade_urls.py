from django.urls import path
from atividades.views.atividade_views import *
from atividades.views.usuario_view import *

urlpatterns = [
    path('cadastrar/', cadastrar_atividade, name='cadastrar_atividade'),
    path('editar/<int:id>/', editar_atividade, name='editar_atividade'),
    path('listar/', listar_atividades, name='listar_atividades'),
    path('listar/ano_<int:ano>/<str:tipo>_<int:valor>/', listar_tipo, name='listar_tipo'),
    path('listar/ano_<int:ano>/', listar_ano, name='listar_ano'),
    path('listar/semana_atual/', listar_semana_atual, name='listar_semana_atual'),
    path('listar/<int:id>', expandir_atividade, name='expandir_atividade'),

    path('listar_data/<str:data>/', listar_por_data, name='listar_por_data'),
    path('area/<str:area>/', listar_por_area, name='listar_por_area'),
    path('sub-area/<str:sub_area>/', listar_por_sub_area, name='listar_por_sub_area'),
    path('plataforma/<str:plataforma>/', listar_por_plataforma, name='listar_por_plataforma'),
    path('pessoa/<str:pessoa>/', listar_por_pessoa, name='listar_por_pessoa'),
    path('descricao/<str:descricao>/', listar_por_descricao, name='listar_por_descricao'),

    path('remover/<int:id>', remover_atividade, name='remover_atividade'),

    # USUÁRIOS
    path('usuarios/cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/logar/', logar_usuario, name="logar_usuario"),
    path('usuarios/logout/', deslogar_usuario, name='deslogar_usuario'),
]
