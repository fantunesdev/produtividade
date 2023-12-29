from django.urls import path
from ..views.pessoa_views import *

urlpatterns = [
    path('', listar_pessoas, name='listar_pessoas'),
    path('cadastrar/', cadastrar_pessoa, name='cadastrar_pessoa'),
    path('editar/<int:id>', editar_pessoa, name='editar_pessoa'),
    path('remover/<int:id>', remover_pessoa, name='remover_pessoa')
]
