from django.urls import path
from ..views.sub_area_views import *


urlpatterns = [
    path('cadastrar/', cadastrar_sub_area, name='cadastrar_sub_area'),
    path('listar', listar_sub_areas, name='listar_sub_areas'),
    path('listar/<int:id>/', listar_sub_area_id, name='listar_sub_area_id'),
    path('<str:nome>/', listar_sub_area_nome, name='listar_sub_area_nome'),
    path('editar/<int:id>/', editar_sub_area, name='editar_sub_area'),
    path('remover/<int:id>/', remover_sub_area, name='remover_sub_area'),
]
