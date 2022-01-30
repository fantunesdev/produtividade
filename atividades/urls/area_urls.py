from django.urls import path
from atividades.views.area_views import *

urlpatterns = [
    path('cadastrar/', cadastrar_area, name='cadastrar_area'),
    path('listar/', listar_areas, name='listar_areas'),
    path('listar/<str:nome>/', listar_area, name='listar_area'),
    path('listar/<int:id>/', listar_area_id, name='listar_area_id'),
    path('editar/<int:id>/', editar_area, name='editar_area'),
    path('remover/<int:id>/', remover_area, name='remover_area'),
]
