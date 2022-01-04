from django.urls import path
from atividades.views.usuario_view import *

urlpatterns = [
    path('cadastrar/', cadastrar_usuario, name='cadastrar_usuario')
]