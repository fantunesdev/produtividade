from django.urls import path

from atividades.views.area_views import *

urlpatterns = [
    path('cadastrar/', cadastrar_area, name='cadastrar_area'),
    path('', listar_areas, name='listar_areas'),
    path('editar/<int:id>/', editar_area, name='editar_area'),
    path('remover/<int:id>/', remover_area, name='remover_area'),
]
