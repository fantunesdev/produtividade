from django.urls import path

from atividades.views.subarea_views import *


urlpatterns = [
    path('cadastrar/', cadastrar_subarea, name='cadastrar_subarea'),
    path('', listar_subareas, name='listar_subareas'),
    path('<int:id>/', listar_subarea_id, name='listar_subarea_id'),
    path('editar/<int:id>/', editar_subarea, name='editar_subarea'),
    path('remover/<int:id>/', remover_subarea, name='remover_subarea'),
]
