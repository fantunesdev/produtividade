from django.urls import path
from atividades.views.plataforma_view import *

urlpatterns = [
    path('', listar_plataformas, name='listar_plataformas'),
    path('cadastrar/', cadastrar_plataforma, name='cadastrar_plataforma'),
    path('editar/<int:id>/', editar_plataforma, name='editar_plataforma'),
    path('remover/<int:id>/', remover_plataforma, name='remover_plataforma')
]
