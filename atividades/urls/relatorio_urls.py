from django.urls import path

from atividades.views.relatorio_views import *

urlpatterns = [
    path('', relatorios, name='relatorios')
]
