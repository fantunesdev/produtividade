from django.urls import path
from .views.atividade_views import *
from .views.area_views import *
from .views.plataforma_view import *
from .views.usuario_view import *

urlpatterns = [
    path('listar/ano_<int:ano>/<str:tipo>_<int:valor>/', listar_tipo, name='listar_tipo'),
    path('listar/ano_<int:ano>/', listar_ano, name='listar_ano'),

    path('cadastrar/', cadastrar_atividade, name='cadastrar_atividade'),
    path('listar/', listar_atividades, name='listar_atividades'),
    #path('listar/ano/<int:ano>/', listar_por_ano, name='listar_por_ano'),
    #path('listar/mes/<int:mes>/', listar_por_mes, name='listar_por_mes'),
    path('listar/semana_atual/', listar_semana_atual, name='listar_semana_atual'),
    #path('listar/semana/<int:semana>/', listar_por_semana, name='listar_por_semana'),
    path('listar_data/<str:data>/', listar_por_data, name='listar_por_data'),
    path('listar/<int:id>', expandir_atividade, name='expandir_atividade'),
    path('area/<str:area>/', listar_por_area, name='listar_por_area'),
    path('sub-area/<str:sub_area>/', listar_por_sub_area, name='listar_por_sub_area'),
    path('plataforma/<str:plataforma>/', listar_por_plataforma, name='listar_por_plataforma'),
    path('pessoa/<str:pessoa>/', listar_por_pessoa, name='listar_por_pessoa'),
    path('descricao/<str:descricao>/', listar_por_descricao, name='listar_por_descricao'),
    path('editar/<int:id>/', editar_atividade, name='editar_atividade'),
    path('remover/<int:id>', remover_atividade, name='remover_atividade'),

    path('areas/cadastrar/', cadastrar_area, name='cadastrar_area'),
    path('areas/listar/', listar_areas, name='listar_areas'),
    path('areas/listar/<str:nome>/', listar_area, name='listar_area'),
    path('areas/listar/<int:id>/', listar_area_id, name='listar_area_id'),
    path('areas/editar/<int:id>/', editar_area, name='editar_area'),
    path('areas/remover/<int:id>/', remover_area, name='remover_area'),

    path('plataformas/cadastrar/', cadastrar_plataforma, name='cadastrar_plataforma'),
    path('plataformas/listar/', listar_plataformas, name='listar_plataformas'),
    path('plataformas/listar/<int:id>/', listar_plataforma_id, name='listar_plataforma_id'),
    path('plataformas/listar/<str:nome>/', listar_plataforma_nome, name='listar_plataforma_nome'),
    path('plataformas/editar/<int:id>/', editar_plataforma, name='editar_plataforma'),
    path('plataformas/remover/<int:id>/', remover_plataforma, name='remover_plataforma'),

    path('usuarios/cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/logar/', logar_usuario, name="logar_usuario"),
    path('usuarios/logout/', deslogar_usuario, name='deslogar_usuario'),
]